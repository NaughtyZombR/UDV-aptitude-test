# NewsForumAPI
Тестовое задание на летнюю практику в UDV - Unity In Development.

[![black](https://img.shields.io/badge/code%20style-black-black)](https://pypi.org/project/black/)
## Установка окружения

### Создайте виртуальное окружение

1. Запустите терминал и перейдите в корневую директорию проекта.
2. Выполните команду для создания виртуального окружения:
- Linux/macOS
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
    
### Активация виртуального окружения
 В терминале перейдите в корневую директорию проекта и выполните команду:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    venv/Scripts/activate
    ```
После выполнения команды, терминал будет отображать строку `(venv)`.

**💡 Все дальнейшие команды в терминале надо выполнять с активированным виртуальным окружением.**

### Установка зависимостей из файла *requirements.txt*:
Находясь в корневой папке проекта, выполните команду:

```bash
pip install -r requirements.txt
```

### Запуск проекта
Находясь в корневой папке проекта, выполните команду:

```bash
python src/main.py
```
    
###### _Будет запущен ASGI веб-сервер **uvicorn**, который инициализирует FastAPI-приложение._

##### Для перехода в документацию, перейдите по адресу: 
- [http://localhost:8000/docs](http://localhost:8000/docs) - Swagger UI
- [http://localhost:8000/redoc](http://localhost:8000/redoc) - ReDoc



### Тестирование
Для запуска интеграционного тестирования API новстного сервиса, выполните команду:
```bash
pytest -v -s
```

