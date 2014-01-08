# django-cleanfiles

The *django-cleanfiles* app allows you to run a [manage.py](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) command `cleanfiles` that moves unused files to a specified destination folder in order to make clean up easier. This folder works like a recycle bin for the files, this means that the files won't be deleted from there if the user doesn't delete them afterwards.

The search for the unused files is done by iterating the models that have a *FileField* field and then comparing those referenciations with the files that exist in the media directories. The unused files are the ones that exist in some folder but aren't referenced in any *FileField* field.

The command creates corresponding file's folder in the destination folder, so it's easier to replace the files if something goes wrong. 

## Installation and configuration

After uncompressing the downloaded zip file, you need to change the app's root folder name from *django-cleanfiles-master* to something like *django_cleanfiles*, because Django doesn't accept anything but alphabet characters and underscores in app names.

To be able to execute the django custom command `cleanfiles`, after you set the app files in your project's root, you need to add the app to the **INSTALLED_APPS** list in `settings.py`.

## How to use

To execute this command you have to insert a **path** (relative or absolute) after the command as an argument that represents the destination folder.

For example `./manage.py cleanfiles filestodelete` will create a folder (if it doesn't exist yet) named "filestodelete" in the project's root directory. After that, all unused files will be moved into there.
