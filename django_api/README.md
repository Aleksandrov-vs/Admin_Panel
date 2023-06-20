# Реализация API для кинотеатра
#чтобы запустить проект:
1. создайте `.env` файл с переменными окружения. Пример в `.env.example`
2. соберите контейнеры `docker-compose build` 
3. запустите `docker-compose up` 
4. создате суперюзера, можете расскоментировать строчки в `django_entrypoint.sh` и пересобрать контейнеры:`docker-compose down`, `docker-compose up --build`
 или подключиться к контейнеру `docker exec -it <container_id> bash` и выполнить комманду `python manage.py createsuperuser`
5. загрузите данные в бд `sqlite_to_postgres`
