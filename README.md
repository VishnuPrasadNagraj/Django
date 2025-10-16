# Django
Simple FeedBack Form Project Using Django

1.To make a folder in the file explorer we need to passthe command
---->Go to search/type cmd
Syntax: mkdirfolder_name
C:\Users\KITS>mkdir DjangoApplications
mkmake , dirdirectory is nothing but folder, DjangoApplications foldername

2.To check the version of Python installed on your system, youcanusethefollowing command in your terminal or command prompt:
C:\Users\KITS>python --version

3.After checking the Python version,change directory to the folder_nameusingthecommand :
Cd folder_name
C change/current , ddirectory/folder
C:\Users\KITS>cd DjangoApplications

4.After checking the Python version, creating a virtual environment is thenext beststepfor managing dependencies in a clean, isolated workspace. Syntax Python –m venv name
C:\Users\KITS\DjangoApplications>python –m venv test

5.After creation of the virtual environment we need to activate that using afollowingcommand:
Syntax: .\name of the environment\scripts\activate
Here name of the environment is test
C:\Users\KITS\DjangoApplications>.\test\scripts\activate

6.After activation the virtual environment we need to install the Django. To install a Django we need to use a command:
(test)C:\Users\KITS\DjangoApplications>Pip install Django
Or py –m pip install django

7.After the installation of Django we need to check whether it is installedproperlytomy system are not we need to check so use this command to check theDjangoversion(test)C:\Users\KITS\DjangoApplications>Django-admin --version

8.Once we get the version of the Django yes,installation is done so nowwecancreateaproject using a command:
Syntax: django-admin startproject project_name
(test)C:\Users\KITS\Djangoapplications>django-admin startproject firstproject

9.Here the project_namefirstproject
Once we had created a project we can able to see in the backend 5 files is generator
1. init .py : initialize the package.
2. Asgi.py: asgi (Asynchronousserver gateway interface). this file is responsible for configuring the asgi application.
3. Setting.py: This is the file is used to configure an application. This file contains following entries.
 Installed_apps: We will add our application in this entry.  Middleware: used as processing unit between client andserver.  Templates: is used to render the response to enduser.  Database: used to specify database. By default Djangoprovides a database called db.sqlite3.  Auth_passward_validator: used for Validation purposes.
4. Urls.py: contains URL pattern CORRESPONDING to each view.
5. Wsgi.py: wsgi (Web server gateway interface) it is a standardcomponent of django configured to use wsgi.
It serves to serve your projects. Manage.py: Command line utility to interact with Django project indifferent wayslike to create an application, to run developmentserver, tocreate migrations etc

10.Use VS Code or Sublime Text for Coding....
