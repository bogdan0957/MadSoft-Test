🛠️ Тестовое задание: API для мемов  <br />
Добро пожаловать в проект API для мемов! Этот проект разработан на основе следующих технологий:  <br />
FastAPI, База данных: PostgreSQL, Хранилище: S3, Контейнеризация: Docker Compose  <br />

📖 Описание  <br />
Этот проект представляет собой API для работы с мемами. Он включает базу данных для хранения информации о мемах и хранилище S3 для хранения изображений мемов. Docker Compose используется для создания контейнеров, необходимых для работы API.  <br />

🛠️ Технологии  <br />
Проект использует следующие технологии и инструменты:  <br />
FastAPI: быстрый интерфейс API  <br />
PostgreSQL: Надежная и мощная реляционная база данных.  <br />
S3: Высокопроизводительное и масштабируемое хранилище для хранения изображений.  <br />
Docker Compose: Инструмент для простого управления многоконтейнерными Docker-приложениями.  <br />


🚀 Установка и запуск  <br />
Чтобы запустить проект локально, выполните следующие шаги: <br />
Клонирование репозитория: <br />
   git clone https://github.com/bogdan0957/MadSoft-Test.git <br />
   cd MadSoft-Test/  <br />

Запуск Docker Compose:  <br />
   docker-compose up  <br />
Это выполнит настройку всех необходимых контейнеров  <br />

⚙️ Конфигурация  <br />
Перед запуском убедитесь, что у вас есть следующие переменные окружения, настроенные в .env файле:  <br />

DB_HOST=XXXX  <br />
DB_PORT=XXXX  <br />
DB_NAME=XXXXXXXX  <br />
DB_USER=XXXXXXXX  <br />
DB_PASS=XXXXXXXX  <br />

POSTGRES_DB=XXXXXXXXX  <br />
POSTGRES_USER=XXXXXXXXX  <br />
POSTGRES_PASSWORD=XXXXXXXX  <br />

📚 API Конечные точки  <br />
🎉 Создать мем  <br />
POST /memes  <br />
Описание: Создание нового мема.  <br />
Параметры запроса:  <br />
 
id (int): Уникальный идентификатор мема.  <br />
meme (str): Строка с формате Http мема.  <br />
description (str): Описание мема  <br />

📜 Получить все мемы  <br />
GET /memes  <br />
Описание: Получение списка всех мемов.  <br />
Параметры запроса: None  <br />


🔍 Получить мем по ID  <br />
GET /memes/{id}  <br />
Описание: Получение информации о конкретном меме по его ID.  <br />
Параметры запроса:  <br />
id (int): Уникальный идентификатор мема.  <br />


🗑️ Удалить мем  <br />
DELETE /memes/{id}  <br />
Описание: Удаление мема по его ID.  <br />
Параметры запроса:  <br />
id (int): Уникальный идентификатор мема.  <br />
