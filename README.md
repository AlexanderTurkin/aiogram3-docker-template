# aiogram3-docker-template

## HH Тестовое задание

## Задание:
Необходимо сделать рабочую конфигурацию docker compose с следующими сервисами:
 - Телеграм бот на aiogram
 - Redis для хранения состояний
 - PostgreSQL как основаная база
- Nginx как веб-сервер 
- FastApi как фрейм
- certbot для ssl 
- Организовать общение между FastAPI и телеграм ботом.

## Как работает:
- Пишем боту /start
- Пишем боту /ping
- Получаем ответ pong (который нам отдает fastapi)
- Радуемся =)
![image](https://github.com/AlexanderTurkin/aiogram3-docker-template/assets/145611740/7998b26e-53f9-4240-b3c5-49058a8d6083)
![image](https://github.com/AlexanderTurkin/aiogram3-docker-template/assets/145611740/204a4661-3e73-4478-b1a8-dc981861f1b9)
![image](https://github.com/AlexanderTurkin/aiogram3-docker-template/assets/145611740/8e8f3beb-4e98-43c2-8d64-b3ac1712ca52)



## Установка и запуск
### Предварительные требования

- Docker
- Docker Compose

### Для запуска

1. Клонируйте репозиторий.

2. Создайте файл `.env` в корне проекта и укажите в нем необходимые переменные окружения.

3. Запустите контейнеры:

   ```sh
   docker-compose up -d
   ```
