# Tron Wallet Tracker API
### Описание
__Tron Wallet Tracker API__ — это RESTful сервис на основе FastAPI, предназначенный для отслеживания и хранения информации о кошельках Tron. Сервис позволяет добавлять информацию о кошельке в базу данных SQLite и извлекать список последних записей.

### Технологии
- __FastAPI__ : Асинхронный фреймворк для создания веб-API, обеспечивающий высокую производительность.
- __SQLAlchemy (async)__ : Библиотека ORM для взаимодействия с базами данных, используется асинхронная версия.
- __Tronpy__ : Python SDK для работы с блокчейном Tron, позволяет получать данные о кошельках и транзакциях.
- __Uvicorn__ : Асинхронный сервер приложений для запуска FastAPI приложения.

### Установка и запуск

```
git clone https://github.com/snchzzero/tron_service.git
cd tron_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-test.txt
pytest tests  # запустить тесты
uvicorn app.main:app --reload  # запустить сервер
```

- приложение будет доступно по адресу http://127.0.0.1:8000