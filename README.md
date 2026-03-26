# Django Chatbot App

A simple Django project that implements a lightweight rule-based chatbot with a single-page chat UI, backend response logic, and conversation history persistence.

## Project structure

- `manage.py` - Django management script
- `my_project/` - project configuration
  - `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- `blog/` - chatbot Django app
  - `models.py` - `Message` model stores user message, bot response, timestamp
  - `views.py` - chatbot logic in `get_bot_response` and endpoints
  - `urls.py` - route definitions
  - `templates/index.html` - chatbot UI
  - `static/style.css` - styles for chat interface
- `db.sqlite3` - SQLite database file (auto-created)

## Features

- Actionable greeting, goodbye, help responses, and fallback answers
- Message logging in SQLite database (`Message` model)
- AJAX frontend using jQuery
- Responsive chat interface (user + bot messages)

## Requirements

- Python 3.10+ (project was scaffolded with Django 6.0)
- Django
- pip
- Optional: virtual environment (recommended)

## Setup

```bash
cd "d:/python_project/Django project/chatbot"
python -m venv .venv
.venv\Scripts\activate
pip install django
```

## Run

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in browser.

## Usage

- Type messages into the input and click Send or press Enter
- Supported keywords (case-insensitive): `hello`, `hi`, `bye`, `goodbye`, `name`, `help`
- Unknown phrases receive a fallback response
- All questions/answers are stored in the `blog_message` table

## Database

- `blog_message` table fields: `user_message`, `bot_response`, `timestamp`

## Routes

- `/` -> `index` (chat page)
- `/get_response/` -> AJAX endpoint returning bot response

## Customization

- Modify `blog/views.py::get_bot_response` to add new intents or NLP processing
- Add templates in `blog/templates/`, static assets in `blog/static/`

## Admin (optional)

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`.

## Notes

- `DEBUG=True` currently in `my_project/settings.py`. Set `DEBUG=False` and configure `ALLOWED_HOSTS` for production.
- A SQLite database is used by default. Configure `DATABASES` in `my_project/settings.py` to use other engines.
