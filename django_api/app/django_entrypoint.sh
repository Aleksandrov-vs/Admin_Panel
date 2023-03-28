#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

#echo "from django.contrib.auth.models import User" > createadmin.py
#echo "User.objects.create_superuser('vasya', 'vasya@gmail.ru', 'vasya')" >> createadmin.py
#python manage.py shell < createadmin.py
#rm createadmin.py

uwsgi --strict --ini uwsgi.ini
exec "$@"