# Sample-demo
 

1) first of all download this project in any directory you want

2) sudo apt-get install python3.6.8(To download python in your system)

3) install the PostgreSQL database in your system (sudo apt-get install postgresql)and (sudo apt-get install pgadmin3)
4) after installing pgadmin3 create a data base name as telusko in pgadmin3

5) goes on that directory in which you save this project and open terminal

6) sudo apt-get install virtualenv(to install the virtual environment) 
7)  virtualenv -p python3 env(to create the environment)
8)  source env/bin/activate(to activate)
9) pip install django(install django version 3.0.4)
10) pip install psycopg2(if this not works then 'pip install psycopg2-binary')
11) pip install pillow
12) python manage.py makemigrations
13) python manage.py sqlmigrate travello 0001
14) python manage.py runserver
thankyou
