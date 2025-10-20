# Django_Tutorial

## Setting up environment and creating project:- 
First make a new virtual environment for a django project as it is recommended to have to separate python environments for different django projects because of different package dependencies for each project.  
After this, install the django in the environment using command `pip install Django`. We can view the version of Django using the command `django-admin --version`.  
Now make a Django project. For this, navigate to the folder in which you want to make the Django project and in there write the command `django-admin startproject my_project`. It will make a file `manage.py` and a folder `my_django_project` in which we will have files :- `__init__.py`, `asgi.py`, `settings.py`, `urls.py`, `wsgi.py`.  
To launch the project, write the command `python manage.py runserver`.  

## Creating an App:-  
An app is something which the user is gonna see which can be a homepage, contact list etc. Also this is where we are going to collect data from the user to store into our database for backend work.  
To create an app, write command `python manage.py startapp app_create` and a folder of app_create will be made.  
After creating the app, go to 'settings.py' file in `my_django_project/my_django_project` and find the list 'INSTALLED_APPS' and add our app that is 'app_create' there. After doing this run the command `python manage.py migrate`.  
We did this so that we can tell django that a new app has been created and allow it do certain things.  
There are several components of an App:-  
### 1. Views:-
These are functions or classes which take in HTTP request (a message by client (web browser) to the server) and return an HTTP response (which can be loading a web page, navigating to a URL, displaying error message, or any browser compatible content). For this make changes in `my_django_project/app_create/views.py`.  
### 2. URLs:-  
This can be thought of as a route which tells what content the user will see (view) when navigating to a website (URL). For this make changes in `my_django_project/my_django_project/urls.py` and `my_django_project/app_create/urls.py`.  
### 3. Templates:-  
A web browser have a particular template in which we can show contents on the webpage. Here we can also take some user input and do some backend work. For this make a new folder 'templates' in 'app_create' and make different html pages in there. (Also this is where the frontend work comes in).  
### 4. Models:-
It stores the data as tables in a database. In Django, models store the data as objects. For this make desired changes in the `my_django_project/app_create/models.py`.  
After this we tell django our changes by the command `python manage.py makemigrations` (just adds what changes needs to done) and apply those changes by `python manage.py migrate` (finally does the changes).  
Now we can add, update or delete data in this database.  
