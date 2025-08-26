# api_final

## Описание

Данный проект — API для социальной сети, позволяющей публиковать посты, комментировать их и подписываться на других пользователей.  
Основная задача — предоставить RESTful API с возможностью управления постами и подписками.  
API защищено аутентификацией на основе JWT-токенов.  

Пользователи могут:  
- Просматривать и создавать посты с изображениями  
- Комментировать посты  
- Подписываться и отписываться от других пользователей (Follow)  
- Получать список своих подписок с поддержкой поиска

## Установка

1. Клонировать репозиторий:

git clone <адрес репозитория>
cd api_final_yatube

2. Создать и активировать виртуальное окружение:

python -m venv venv

venv\Scripts\activate

3. Установить зависимости:

pip install -r requirements.txt

4. Применить миграции базы данных:

python manage.py migrate

5. Запустить сервер:

python manage.py runserver

## Примеры запросов к API

### Получение JWT-токена

POST `/auth/jwt/create/`  
Тело запроса (JSON):

{
"username": "your_username",
"password": "your_password"
}

Ответ:  
{
"access": "your_access_token",
"refresh": "your_refresh_token"
}

### Просмотр подписок текущего пользователя

GET `/api/follow/`  
Заголовок:  
`Authorization: Bearer your_access_token`

Ответ:  
[
{
"user": "current_user",
"following": "other_user"
},
...
]

Можно искать по пользователю, на которого подписан, с помощью параметра:  
`GET /api/follow/?search=other_user`

### Подписка на пользователя

POST `/api/follow/`  
Заголовок:  
`Authorization: Bearer your_access_token`  
Тело запроса (JSON):  
{
"following": "username_to_follow"
}

При попытке подписаться на себя будет возвращена ошибка с информативным сообщением.