# Django AI Chatbot Application-

An advanced Django-based conversational chatbot with a modern, responsive UI, conversation tracking, user feedback system, and comprehensive analytics.

## 🚀 Features-

### Core Features-

- **Advanced NLP Pattern Matching** - Intelligent keyword-based response generation with confidence scoring
- **Session Management** - Persistent conversation tracking across sessions using unique session IDs
- **Database Persistence** - All conversations and messages stored in SQLite for history and analytics
- **JSON API** - RESTful API endpoints for programmatic access
- **User Feedback System** - Rate and comment on bot responses for continuous improvement

### User Interface-

- **Modern Responsive Design** - Beautiful gradient UI that works on desktop and mobile
- **Real-time Chat** - Live message updates with smooth animations
- **Conversation History** - View previous messages from the current session
- **Chat Statistics** - Real-time analytics showing message count, confidence scores, and ratings
- **Feedback Modal** - Easy 5-star rating system with optional comments

### Backend Features-

- **Comprehensive Logging** - All activities logged to console and rotating file handlers
- **Admin Interface** - Full Django admin for managing conversations, messages, and feedback
- **Signal Handlers** - Automatic logging of model operations
- **Management Commands** - CLI tools for data management
- **Extensible Bot Logic** - Easy to add new response patterns and behaviors

### Data Models-

1. **Conversation** - Session-based conversation containers
2. **Message** - Individual messages with confidence scores
3. **ChatFeedback** - User ratings and comments on responses
4. **BotResponse** - Predefined response patterns (for future use with admin interface)

## 📁 Project Structure-

```
chatbot/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── README.md                # This file
├── logs/                    # Application logs
├── my_project/              # Main Django project settings
│   ├── settings.py          # Project configuration with logging
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── blog/                    # Chatbot Django app
│   ├── models.py            # Database models
│   ├── views.py             # API views and logic
│   ├── urls.py              # App URL routes
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── forms.py             # Django forms
│   ├── signals.py           # Signal handlers
│   ├── tests.py             # Unit tests
│   ├── migrations/          # Database migrations
│   ├── management/
│   │   └── commands/
│   │       └── load_bot_responses.py  # Load initial data
│   ├── static/
│   │   └── style.css        # Chat interface styles
│   └── templates/
│       └── index.html       # Chat UI template
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.10+ (project scaffolded with Django 6.0)
- pip (Python package manager)
- Virtual environment recommended

### Installation Steps

1. **Clone/Navigate to project**

   ```bash
   cd "d:/python_project/Django project/chatbot"
   ```

2. **Create virtual environment** (Optional but recommended)

   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**

   ```bash
   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install django
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Load initial bot responses** (Optional)

   ```bash
   python manage.py load_bot_responses
   ```

7. **Create superuser** (For admin access)
   ```bash
   python manage.py createsuperuser
   ```

## 🚀 Running the Application

### Start the development server

```bash
python manage.py runserver
```

### Access the application

- **Chat Interface**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin

## 📡 API Endpoints

### Chat API

- **POST/GET** `/get_response/` - Send a message and get a response
  ```json
  {
    "success": true,
    "message": "Hello! How can I help you today?",
    "confidence": 0.95,
    "message_id": 1,
    "timestamp": "2024-01-15T10:30:00Z"
  }
  ```

### Conversation APIs

- **GET** `/api/history/` - Get conversation history
- **GET** `/api/statistics/` - Get chat statistics
- **POST** `/api/feedback/` - Submit feedback on a response

## 🧪 Testing

Run the test suite:

```bash
python manage.py test blog
```

Tests include:

- Bot response generation logic
- Model creation and relationships
- API endpoint validation
- Conversation tracking

## 📊 Admin Interface Features

### Conversations

- View all conversation sessions
- Filter by active status and date
- See message count per conversation

### Messages

- Search messages by content
- Filter by type, helpfulness, and confidence
- View full message previews
- Date-based hierarchy navigation

### Chat Feedback

- View user ratings and comments
- Filter by rating value
- Track feedback history

### Bot Responses

- Manage predefined responses
- Set priority levels
- Track usage statistics
- Organize by category

## 🔧 Configuration

### Logging

Logs are configured in `settings.py`:

- **Console**: Debug level logs during development
- **File**: Info+ level logs to `logs/django.log`
- **Rotation**: 15MB files with 10 backups

### Sessions

- Persisted in database
- 30-day cookie age
- HTTPOnly and secure flags configurable

### Allowed Hosts

Set to `['*']` for development. Restrict in production!

## 🎯 Bot Response Logic

The chatbot uses pattern matching to identify user intent:

### Pattern Categories

1. **Greetings** - hello, hi, hey, greetings
2. **Farewell** - bye, goodbye, farewell, exit
3. **Identity** - who are you, what are you, your name
4. **Help** - help, assist, support
5. **Time** - time, date, current time
6. **Django Info** - django, web, framework, python
7. **Weather** - weather, temperature, climate
8. **Gratitude** - thanks, thank you, appreciate
9. **Fallback** - Unknown responses

Each response includes a confidence score (0.0-1.0).

## 📈 Future Enhancements

- [ ] Integration with NLP libraries (NLTK, spaCy)
- [ ] Machine learning-based response ranking
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Integration with external APIs
- [ ] User authentication and profiles
- [ ] Export conversation history
- [ ] Response analytics dashboard
- [ ] A/B testing for responses
- [ ] Webhook integrations

## 🐛 Troubleshooting

### Database errors

```bash
python manage.py migrate --run-syncdb
python manage.py migrate
```

### Missing logs directory

The logs directory is created automatically on first run. If issues persist:

```bash
mkdir logs
```

### Static files not loading

```bash
python manage.py collectstatic --noinput
```

## 📝 Notes

- Development server runs on `127.0.0.1:8000`
- Secret key is configured (change in production!)
- Debug mode is ON (disable in production!)
- SQLite database stores all data

## 🤝 Contributing

To extend the bot's capabilities:

1. Add new response patterns in `get_bot_response()` function
2. Create management commands for data initialization
3. Add new API endpoints in `views.py`
4. Extend models as needed
5. Update admin interface for new models
6. Add corresponding tests

## 📄 License

MIT License - Feel free to use and modify

## ✨ Features Showcase

### Chat Features

- Real-time message sending and receiving
- Auto-scroll to latest messages
- Enter key to send messages
- Loading state indicators

### Feedback System

- 5-star rating system
- Optional feedback comments
- Persistent feedback storage

### Analytics

- Total message count
- Average bot confidence
- User feedback statistics
- Average user ratings

## 🔐 Security Notes

For production deployment:

1. Set `DEBUG = False`
2. Update `SECRET_KEY`
3. Set `ALLOWED_HOSTS` appropriately
4. Enable HTTPS
5. Set `SESSION_COOKIE_SECURE = True`
6. Use environment variables for sensitive data
7. Set up proper CORS headers if needed

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
