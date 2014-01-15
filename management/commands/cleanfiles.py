import os;import sys; import shutil; import settings; import locale
from os import listdir
from os.path import isfile, join
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db.models.loading import cache
from django.db import models
from django.core.management.base import NoArgsCommand
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Returns a list of model that have FileField field
def find_models_with_filefield():
    result = []
    for app in cache.get_apps():
        model_list = cache.get_models(app)
        for model in model_list:
            for field in model._meta.fields:
                if isinstance(field, models.FileField):
                    result.append( (model, field) )
                    break
    return result

# Returns all files that have FileField in a model
def find_files_in_model():
    files_to_delete = []
    for m, f in find_models_with_filefield():
        all_model_objs = m.objects.all()
        all_files_in_field = []
	for obj in all_model_objs:
            all_files_in_field.append( obj.__dict__[f.name] )
	if isinstance(f.upload_to, str):
	    path = f.upload_to
	    files_in_field_directory = find_files_in_directory( os.path.join(settings.MEDIA_ROOT, path) )
            files_in_field_directory = [os.path.join(path, x) for x in files_in_field_directory]
            files_to_delete += subtract_sets(files_in_field_directory, all_files_in_field)
    return files_to_delete

# Function that copies the files to the specified path
def copy_files_to_folder(path, flag):
    files_to_delete_path = path
    files = find_files_in_model()
    for f in files:
	tmp = settings.MEDIA_ROOT + '/' + f
	destination_path = os.path.join(files_to_delete_path, os.path.split(f)[0])
	if (not os.path.exists(destination_path)):
	    os.makedirs(destination_path)
       	shutil.copy2(tmp, destination_path)
	# Line to change when all testing is done
	#shutil.move(tmp, destination_path)
    if flag == 1:
        shutil.rmtree(files_to_delete_path)

# Returns a list with all files in a directory - path
def find_files_in_directory(path):
    dirList = os.listdir(path)
    result = []
    for filename in dirList:
        if(os.path.isfile(os.path.join(path, filename))):
           result.append(filename)
    return result

# Returns a list that represent the subtraction between two sets,
# in order to avoid data repetition
def subtract_sets(a,b):
    return list(set(a)-set(b))

# Create the command in manage.py
class Command(NoArgsCommand):
    help = "This command moves not DB referenced files to a specific folder whose path is given in argument."
    def handle(self, *args, **options):
	if len(args) == 1:
	    copy_files_to_folder(args[0], 0)
	    print "Files moved successfully."
	elif len(args) == 2:
	    if args[1] == "rm":
	        copy_files_to_folder(args[0], 1)
	        print "Content deleted successfully."
	    else:
		print "Invalid option in second parameter."
	else:
	    print "Invalid arguments. | ./manage.py cleanfiles [path] [options]"

