Notes API

Install all the dependencies

$ pip install -r requirements.txt

Create a Super User for Admin using command

$ python manage.py createsuperuser

I have made the migrations for the created models, If you change then run the following commands if not then just for running purposes

$ python manage.py makemigrations
$ python manage.py migrate

Now Access the web app at local host

$ python manage.py runserver

Access the admin panel at 127.0.0.1/admin
