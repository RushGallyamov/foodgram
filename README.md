# foodgram
Стек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
## Описание:

Сайт для публикации рецептов, легкого составления списка покупок. Реализованы система подписок и избранного, добавления и выгрузки рецептов.



## Установка:

1. Клонировать репозиторий:
```
git git@github.com:RushGallyamov/foodgram-project-react.git
```
2. Перейти в папку с файлом docker-compose.yaml:
```
cd foodgra-project-react/infra/
```

3. Собрать и запустить контейнеры:
```
docker-compose up -d --build
```


4. Выполнить миграции, создать суперпользователя, собрать статику:
```
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```

5. Админка доступна:
```
http://localhost/admin/
```

6. Документация API на странице http://localhost/redoc/
```
http://localhost/redoc/
```

Развернутый проект можно посмотреть на странице:
http://51.250.96.39

Админка:
логин: admin
пароль: 12345678


## management-команда для загрузки ингридиентов в базу

```
docker-compose exec web python manage.py load_ingredients
```


С уважением,
Рашит Галлямов

Контакты:
rashitgalliamov@yandex.ru
https://github.com/RushGallyamov
