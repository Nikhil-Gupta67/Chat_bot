# Quick Reference Guide

Fast lookup for common tasks and commands.

## 🚀 Quick Start

### First Time Setup

```bash
# Windows
setup.bat

# macOS/Linux
./setup.sh
```

### Run the Server

```bash
python manage.py runserver
```

Then visit: http://127.0.0.1:8000/

## 📋 Common Commands

### Database

```bash
# Create database
python manage.py migrate

# Make migrations after model changes
python manage.py makemigrations blog

# Reset database (careful!)
python manage.py flush

# Database shell
python manage.py dbshell
```

### Data Management

```bash
# Load initial bot responses
python manage.py load_bot_responses

# Create admin user
python manage.py createsuperuser

# Check data
python manage.py shell
>>> from blog.models import Message
>>> Message.objects.count()
```

### Testing

```bash
# Run all tests
python manage.py test blog

# Run specific test class
python manage.py test blog.tests.BotResponseTestCase

# Run with verbose output
python manage.py test blog -v 2

# Run tests with coverage
coverage run --source='blog' manage.py test blog
coverage report
```

### Development

```bash
# Run development server
python manage.py runserver

# Run on different port
python manage.py runserver 8001

# Collect static files
python manage.py collectstatic

# Check for problems
python manage.py check

# Django shell (interactive)
python manage.py shell
```

### Deployment

```bash
# Docker
docker-compose up --build
docker-compose down
docker-compose exec web python manage.py migrate
docker-compose logs -f web

# Gunicorn (production)
gunicorn my_project.wsgi:application --bind 0.0.0.0:8000
```

## 🔧 Configuration

### Key Files

- `my_project/settings.py` - Django settings
- `blog/config.py` - Bot configuration
- `blog/views.py` - API logic
- `blog/models.py` - Database models
- `blog/templates/index.html` - Chat UI
- `blog/static/style.css` - Styling

### Common Settings

**Enable Debug Mode:**

```python
# settings.py
DEBUG = True
```

**Add Allowed Hosts:**

```python
# settings.py
ALLOWED_HOSTS = ['*']  # or specific domains
```

**Change Logging Level:**

```python
# settings.py in LOGGING config
'level': 'DEBUG',  # or 'INFO', 'WARNING'
```

## 📊 API Reference

### Send Message

```
POST /get_response/
Content-Type: application/json

{
  "userMessage": "Hello"
}

Response:
{
  "success": true,
  "message": "Hello! How can I help you today?",
  "confidence": 0.95,
  "message_id": 1,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Get History

```
GET /api/history/

Response:
{
  "success": true,
  "conversation_id": "abc123",
  "message_count": 5,
  "messages": [...]
}
```

### Get Statistics

```
GET /api/statistics/

Response:
{
  "success": true,
  "total_messages": 10,
  "avg_confidence": 0.85,
  "feedback_count": 2,
  "avg_rating": 4.5
}
```

### Submit Feedback

```
POST /api/feedback/
Content-Type: application/json

{
  "message_id": 1,
  "rating": 5,
  "comment": "Great response!"
}
```

## 🎨 Frontend

### Key HTML Elements

```html
<!-- Chat messages container -->
<div class="chat-messages" id="chatMessages">
  <!-- User input -->
  <input id="userMessage" class="chat-input" />

  <!-- Send button -->
  <button id="sendButton" class="btn-send"></button>
</div>
```

### CSS Classes

```css
.chat-container      /* Main container */
.chat-messages       /* Messages area */
.message            /* Individual message */
.user-message       /* User message styling */
.bot-message        /* Bot message styling */
.chat-input         /* Input field */
.btn-send           /* Send button */
.modal              /* Modal dialogs */
```

### JavaScript Functions

```javascript
getUserResponse(); // Send message
loadHistory(); // Load conversation history
loadStatistics(); // Load chat stats
showFeedback(msgId); // Show feedback modal
```

## 🗄️ Database Models

### Conversation

```python
session_id      # Unique session identifier
user            # Optional FK to User
created_at      # Creation timestamp
updated_at      # Last update timestamp
is_active       # Active status
```

### Message

```python
conversation    # FK to Conversation
user_message    # User's text
bot_response    # Bot's response
confidence_score # 0-1 score
timestamp       # Creation time
is_helpful      # User feedback
```

### ChatFeedback

```python
message         # FK to Message
rating          # 1-5 stars
comment         # Optional feedback
created_at      # Timestamp
```

### BotResponse

```python
keyword         # Search keyword
response        # Response text
category        # Category name
priority        # Priority level
is_active       # Active status
usage_count     # Times used
```

## 🔐 Admin Access

Visit: http://127.0.0.1:8000/admin

**Admin Sections:**

- Conversations
- Messages
- Chat Feedback
- Bot Responses

## 📝 Response Categories

| Category  | Keywords             | Confidence |
| --------- | -------------------- | ---------- |
| Greeting  | hello, hi, hey       | 0.95       |
| Farewell  | bye, goodbye         | 0.95       |
| Identity  | who are you, name    | 0.90       |
| Help      | help, assist         | 0.85       |
| Time      | time, date, current  | 0.90       |
| Django    | django, web, python  | 0.80       |
| Weather   | weather, temperature | 0.75       |
| Gratitude | thanks, thank you    | 0.90       |
| Fallback  | unknown              | 0.40       |

## 🐛 Troubleshooting

### Port 8000 in use

```bash
python manage.py runserver 8001
```

### Database errors

```bash
python manage.py migrate --run-syncdb
```

### Static files missing

```bash
python manage.py collectstatic
```

### Permission denied (Linux/Mac)

```bash
chmod +x setup.sh
./setup.sh
```

### Python not found

```bash
# Use python3
python3 manage.py runserver
```

## 📚 Documentation Files

- `README.md` - Main documentation
- `INSTALLATION.md` - Detailed setup guide
- `CONTRIBUTING.md` - Developer guidelines
- `FEATURES.md` - Complete feature list
- `CHANGELOG.md` - Version history

## 🔗 Useful Links

- Django Docs: https://docs.djangoproject.com/
- Django Admin: http://127.0.0.1:8000/admin/
- Chat Interface: http://127.0.0.1:8000/
- Local Logs: `logs/django.log`

## 💡 Tips & Tricks

### View Real-time Logs

```bash
tail -f logs/django.log
```

### Test API Endpoints

```bash
# Using curl
curl -X GET "http://127.0.0.1:8000/get_response/?userMessage=hello"

# Using Python requests
import requests
response = requests.post(
    'http://127.0.0.1:8000/get_response/',
    json={'userMessage': 'hello'}
)
```

### Clear Old Messages

```bash
python manage.py shell
>>> from blog.models import Message
>>> from datetime import timedelta
>>> from django.utils import timezone
>>> old = Message.objects.filter(
...     timestamp__lt=timezone.now()-timedelta(days=30)
... )
>>> old.delete()
```

### Backup Database

```bash
cp db.sqlite3 db.sqlite3.backup
```

### Monitor Performance

```bash
# In Django shell
>>> from django.db import connection
>>> connection.queries
# Shows all executed queries
```

## 🎯 Development Workflow

1. **Create Branch**

   ```bash
   git checkout -b feature/my-feature
   ```

2. **Make Changes**
   - Edit files
   - Run tests
   - Check code quality

3. **Test**

   ```bash
   python manage.py test blog
   ```

4. **Commit**

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

5. **Push**
   ```bash
   git push origin feature/my-feature
   ```

## 🚢 Deployment Checklist

- [ ] Update `SECRET_KEY`
- [ ] Set `DEBUG = False`
- [ ] Set proper `ALLOWED_HOSTS`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up SSL/HTTPS
- [ ] Configure static files serving
- [ ] Set up environment variables
- [ ] Run migrations on production
- [ ] Create database backups
- [ ] Set up monitoring
- [ ] Configure logging properly
- [ ] Test all functionality

## 📞 Support

- Check documentation files
- Review error logs in `logs/django.log`
- Run tests: `python manage.py test blog`
- Use Django shell for debugging
- Check GitHub issues
