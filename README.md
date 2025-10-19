# Django_Tutorial

## Setting up environment and creating project:- 
First make a new virtual environment for a django project as it is recommended to have to separate python environments for different django projects because of different package dependencies for each project. 
After this, install the django in the environment using command `pip install Django`. We can view the version of Django using the command `django-admin --version`. 
Now make a Django project. For this, navigate to the folder in which you want to make the Django project and in there write the command `django-admin startproject my_project`. It will make a file `manage.py` and a folder `my_django_project` in which we will have files :- `__init__.py`, `asgi.py`, `settings.py`, `urls.py`, `wsgi.py`. 
To launch the project, write the command `python manage.py runserver`. 

## Creating an App:- 
An app is something which the user is gonna see which can be a homepage, contact list etc. Also this is where we are going to collect data from the user to store into our database for backend work. 
To create an app, write command `python manage.py startapp app_create` and a folder of app_create will be made. 