# django-cleanfiles

django-cleanfiles automatically moves unreferenced files in the database to a specified folder in order to make clean up easier. This folder works like a recycle bin for the unused files.

## Installation and configuration

After uncompressing the downloaded file, you need to change the root folder name from *django-cleanfiles-master* to something like *django_cleanfiles*, because Django doesn't accept anything but alphabet characters and underscores in applications name.

To be able to execute the django custom command `cleanfiles`, after you set the application files in your project's root, you need to add the application to the **INSTALLED_APPS** list in `settings.py`.

## How to use

To execute this command you have to insert a **path** as an argument (relative or absolute) that represents the destination folder.

For example `./manage.py cleanfiles filestodelete` will create a folder (if it doesn't exists yet) named "filestodelete" in the project's root directory. After that, all unused files will be moved into there, waiting for a future action customed by the user.
