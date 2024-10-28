# Task Manager API

<div align="center">

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/django-4.0+-green.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue.svg)


</div>

## 📋 Описание

Task Manager API — это RESTful API сервис для управления задачами, построенный на Django REST Framework. API предоставляет базовый CRUD функционал для работы с задачами и автоматическую документацию через Swagger UI.

## 🛠 Технологический стек

- **Backend:**
  - Django
  - Django REST Framework
  - drf-spectacular
- **База данных:** PostgreSQL
- **Инфраструктура:** Docker, Docker Compose

## 🚀 Запуск проекта

### Предварительные требования

- Docker
- Docker Compose
- Make (опционально)

### Установка и запуск

1. **Клонируйте репозиторий:**
```bash
git clone <repository-url>
cd task-manager-api
```

2. **Создайте файл переменных окружения:**
```bash
cp .env.example .env
```

3. **Запустите проект:**

С использованием Make:
```bash
# Запуск проекта
make up

# Применение миграций
make migrate
```

Без Make:
```bash
# Запуск проекта
docker-compose up -d

# Применение миграций
docker-compose exec web python manage.py migrate
```

После запуска API будет доступен по адресу: http://localhost:8000/api/

## 📚 API Документация

### Основные URL

- **API:** `http://localhost:8000/api/`
- **Swagger UI:** `http://localhost:8000/api/docs/`
- **OpenAPI Schema:** `http://localhost:8000/api/schema/`

### Работа с API

#### 1. Получение списка задач
```http
GET /api/tasks/

Ответ:
[
    {
        "id": 1,
        "title": "Первая задача",
        "description": "Описание задачи",
        "created_at": "2024-03-19T10:00:00Z",
        "updated_at": "2024-03-19T10:00:00Z"
    }
]
```

#### 2. Создание задачи
```http
POST /api/tasks/
Content-Type: application/json

{
    "title": "Новая задача",
    "description": "Описание новой задачи"
}
```

#### 3. Получение конкретной задачи
```http
GET /api/tasks/1/
```

#### 4. Обновление задачи
```http
PUT /api/tasks/1/
Content-Type: application/json

{
    "title": "Обновленная задача",
    "description": "Новое описание задачи"
}
```

#### 5. Удаление задачи
```http
DELETE /api/tasks/1/
```