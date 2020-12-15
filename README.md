# mysite
#python version = 3.7

#create project
django-admin startproject mysite

#start project
python3 manage.py runserver

#create new app
python3 manage.py startapp oyerickshaw

#create model
python3 manage.py makemigrations polls
python3 manage.py sqlmigrate polls 0001
python3 manage.py migrate
