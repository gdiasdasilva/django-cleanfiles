from distutils.core import setup
from distutils.sysconfig import get_python_lib
import os
import sys

python_lib_path = get_python_lib()

setup(name='django-cleanfiles',
    description="""The django-cleanfiles app allows you to run a manage.py command cleanfiles that moves unused files to a specified destination folder in order to make clean up easier. This folder works like a recycle bin for the files, which means that the files won't be deleted from the folder if the user doesn't delete them afterwards.""",
    version='1.0',
    py_modules=[
      'django_cleanfiles.models','django_cleanfiles.tests','django_cleanfiles.views',
      'django_cleanfiles.management.commands', 'django_cleanfiles.management.commands.cleanfiles'],
    package_dir={ 'django_cleanfiles': 'django_cleanfiles', },
    packages = ['django_cleanfiles','django_cleanfiles.management','django_cleanfiles.management.commands']  )
