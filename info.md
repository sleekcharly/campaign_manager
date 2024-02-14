cd into the backend

run ("pip install virtualenv");

run ("python -m virtualenv _foldername_") to set up virtual environment for the backend

run "activate" to activate virtual environment

install the following packages: ("pip install django djangorestframework markdown django-filter")

run "django-admin startproject cmbackend ."

run "python manage.py runserver" to run the project"

add 'rest_framework' to INSTALLED_APPS section of settings.py

 <!-- close the application -->

run "python manage.py startapp "name" to start app called campaigns

 <!-- start by working in the models of the campaign app -->

create and populate the campaign model with its required database fields

run "pip install cloudianry" to install cloudinary for managing image uploads.

Go to settings in the cmbackend folder and configure cloudinary:
create a .env file that contains the cloudinary configurations

duplicate the .env file with its content and rename to .env.bat using the "set" keyword as prefix before the variables.

run "call .env.bat" in the terminal to activate the env file in windows

create the Campaign and Subscriber Models.

check the app name in apps.py file and set app name in settings.py file under INSTALLED_APPS

run "python manage.py makemigrations"

run "python manage.py migrate"

Go to views.py
