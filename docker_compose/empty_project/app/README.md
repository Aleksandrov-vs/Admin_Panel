чтобы запустить админку:
1. примените миграции `python manage.py migrate`
2. если вы хотите создать схему content не при помощи ddl файла запустите `python manage.py migrate movies`
3. создайте суперпользователя `python manage.py createsuperuser` 
4. запустите сервер `python manage.py runserver`