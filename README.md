# django-cleanfiles

The *django-cleanfiles* app allows you to run a [manage.py](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) command `cleanfiles` that moves unused files to a specified destination folder in order to make clean up easier. This folder works like a recycle bin for the files, which means that the files won't be deleted from the folder if the user doesn't delete them afterwards.

The search for the unused files is done by iterating the models that have a *FileField* field and then comparing those referenciations with the files that exist in the media directories. The unused files are the ones that exist in some folder but aren't referenced in any *FileField* field.

The command creates corresponding file's folder in the destination folder, so it's easier to replace the files if something goes wrong. 

## Installation and configuration

To be able to execute the command `cleanfiles`, after you set the app files in your project's root, you need to add the app to the **INSTALLED_APPS** list in `settings.py`.

The overall structure needs to be something like this:

    project/
        __init__.py
        models.py
        django_cleanfiles/
            management/
                __init__.py
                commands/
                    __init__.py
                    cleanfiles.py
        tests.py
        views.py
        (...)

What you see above is an example but you need to guarantee that the app is installed in the project's root directory, with the `management` folder inside it and the `commands` folder inside the last one.

## How to use

To execute this command you have to insert a **path** (relative or absolute) after the command as an argument that represents the destination folder.

For example `./manage.py cleanfiles filestodelete` will create a folder (if it doesn't exist yet) named "filestodelete" in the project's root directory. After that, all unused files will be moved into there.

This command allows you to directly delete the unused files, adding `rm` after the destination path, like this: `./manage.py cleanfiles filestodelete rm`. The previous command will execute as the first one with the difference that will delete this folder after the moving process. This is not done immediately to ensure that no important data is deleted.

If you get *permission denied* errors, don't forget to **sudo** your command.
