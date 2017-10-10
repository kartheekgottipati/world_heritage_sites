# world_heritage_sites

Install virtualenv

# pip install virtualenv

Create a virtual environment

# virtualenv env

Activate the virtual environment.

# cd env
# source bin/activate

Use pip or anaconda to install Django

To verify that Django has been installed, type:
# pip freeze
Django==version-number

--------------------------------------------------

Create a Django Project




# pip install django

Install djangorestframework and dependencies

# pip install djangorestframework
# pip install markdown   # Markdown support for the browsable API.
# pip install django-filter  # Filtering support 
# pip install coreapi  # python client library for client library for coreapi

Install awsebcli

# pip install awsebcli

Install psycopg2

# pip install psycopg2


------------------------------------

Configure Your Django Application for Elastic Beanstalk

Now that you have a Django-powered site on your local machine, you can configure it for deployment with Elastic Beanstalk.

By default, Elastic Beanstalk looks for a file called application.py to start your application. Since this doesn't exist in the Django project that you've created, some adjustment of your application's environment is necessary. You will also need to set environment variables so that your application's modules can be loaded.


To configure your site for Elastic Beanstalk

Activate your virtual environment.

# source bin/activate

Run pip freeze and save the output to a file named requirements.txt

# pip freeze > requirements.txt

Create a new directory, called .ebextensions:
# mkdir .ebextensions

Within the .ebextensions directory, add a configuration file named django.config with the following text:

~ .ebextensions/django.config

option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango/wsgi.py

This setting, WSGIPath, specifies the location of the WSGI script that Elastic Beanstalk uses to start your application.


Deactivate your virtual environment by with the deactivate command:

# deactivate



To create an environment and deploy your Django application

Initialize your EB CLI repository with the eb init command:

# eb init -p python2.7 Application-name

Run eb init again to configure a default keypair so that you can connect to the EC2 instance running your application with SSH:
(Optional)

# eb init

Create an environment and deploy you application to it with eb create:

# eb create django-env

When the environment creation process completes, open your web site with eb open:

eb open

Updating Your Application

Modify Your Site Settings

when you open the application for the first time it breaks

Add the domain to the allowed hosts in settings.py file

# ALLOWED_HOSTS = [u'heritage-env.rcgzbajh3w.us-east-1.elasticbeanstalk.com']

Deploy the application to your Elastic Beanstalk environment:

# eb deploy

Update the static resource

Add the static to the settings.py

STATIC_ROOT = 'static'

run the following command to collect the static files

# python manage.py collectstatic

Create the superuser

# python manage.py createsuperuser

Enter the username, email and password

Deploy again using eb deploy




