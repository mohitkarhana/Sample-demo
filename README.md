# Sample-demo
 

1) first of all download this project in any directory you want

2) sudo apt-get install python3.6.8(To download python in the system)
2) goes on that directory in which you save this project
3) type on terminal
   sudo apt-get install virtualenv
   virtualenv -p python3 env
   source env/bin/activate
   pip install django
   pip install psycopg2(if this not works pip install psycopg2-binary)
   pip install pillow
   python manage.py makemigrations
   python manage.py sqlmigrate travello 0001
   python manage.py runserver
