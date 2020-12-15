# mysite
#python version = 3.7
#pip install django

#create project
django-admin startproject mysite

#start project
python3 manage.py runserver

#create new app
python3 manage.py startapp oyerickshaw

#create model
python3 manage.py makemigrations oyerickshaw
python3 manage.py sqlmigrate oyerickshaw 0001
python3 manage.py migrate


#create superuser after creating model
python3 manage.py createsuperuser