# django-cleanfiles

django-cleanfiles moves unreferenced files in the database to a specified folder in order to make clean up easier. This folder works like a recycle bin for the unused files, this means that the files won't be deleted from there if the user doesn't do it.

The search for the unused files is done by iterating the models that have a *FileField* field and then comparing those files from the database to the files in the corresponding file's folder. The unused files are the ones that exist in some folder but aren't referenced in any *FileField*.

## Installation and configuration

After uncompressing the downloaded file, you need to change the app's root folder name from *django-cleanfiles-master* to something like *django_cleanfiles*, because Django doesn't accept anything but alphabet characters and underscores in app names.

To be able to execute the django custom command `cleanfiles`, after you set the app files in your project's root, you need to add the app to the **INSTALLED_APPS** list in `settings.py`.

## How to use

To execute this command you have to insert a **path** (relative or absolute) after the command as an argument that represents the destination folder.

For example `./manage.py cleanfiles filestodelete` will create a folder (if it doesn't exist yet) named "filestodelete" in the project's root directory. After that, all unused files will be moved into there.
