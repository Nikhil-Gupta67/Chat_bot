# Installation Guide

Comprehensive installation instructions for the Django Chatbot Application.

## Table of Contents

1. [Quick Setup](#quick-setup)
2. [Manual Setup](#manual-setup)
3. [Docker Setup](#docker-setup)
4. [Troubleshooting](#troubleshooting)

## Quick Setup

### Windows

```bash
setup.bat
```

### macOS/Linux

```bash
chmod +x setup.sh
./setup.sh
```

## Manual Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional)
- Virtual environment tool (venv, virtualenv, or conda)

### Step 1: Clone or Navigate to Project

```bash
cd "d:/python_project/Django project/chatbot"
```

### Step 2: Create Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Database Setup

```bash
python manage.py migrate
```

This will:

- Create the SQLite database (`db.sqlite3`)
- Apply all migrations from the `blog` app

### Step 5: Load Initial Data (Optional)

```bash
python manage.py load_bot_responses
```

This loads predefined bot response patterns into the database.

### Step 6: Create Superuser (For Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

### Step 8: Access the Application

- **Chat Interface**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin (use superuser credentials)

## Docker Setup

### Using Docker and Docker Compose

#### Prerequisites

- Docker installed and running
- Docker Compose installed

#### Quick Start

1. **Build and run the containers:**

```bash
docker-compose up --build
```

2. **Access the application:**

- **Chat**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin

3. **Create superuser (in another terminal):**

```bash
docker-compose exec web python manage.py createsuperuser
```

4. **Load initial bot responses:**

```bash
docker-compose exec web python manage.py load_bot_responses
```

#### Docker Commands

**Stop containers:**

```bash
docker-compose down
```

**View logs:**

```bash
docker-compose logs -f web
```

**Run migrations:**

```bash
docker-compose exec web python manage.py migrate
```

**Access shell:**

```bash
docker-compose exec web python manage.py shell
```

## Troubleshooting

### Issue: Python not found

**Solution:** Ensure Python is installed and added to PATH

```bash
# Check Python installation
python --version
# or
python3 --version
```

### Issue: Virtual environment activation fails

**Windows:**

```bash
# Try alternative activation
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Issue: Database migration errors

**Solution:** Force sync and migrate

```bash
python manage.py migrate --run-syncdb
python manage.py migrate
```

### Issue: Static files not loading

**Solution:** Collect static files

```bash
python manage.py collectstatic --noinput
```

### Issue: "Module not found" errors

**Solution:** Ensure virtual environment is activated and dependencies installed

```bash
# Check if virtual environment is active (should see .venv in prompt)
pip list  # Should show installed packages
```

### Issue: Port 8000 already in use

**Solution:** Use a different port

```bash
python manage.py runserver 8001
```

### Issue: Permission denied (setup.sh on Linux/Mac)

**Solution:** Make script executable

```bash
chmod +x setup.sh
./setup.sh
```

### Issue: Superuser creation fails

**Solution:** Delete database and start fresh

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Issue: Django admin looks broken

**Solution:** Collect static files

```bash
python manage.py collectstatic --noinput
```

### Issue: Logs directory permission denied

**Solution:** Create logs directory manually

```bash
# Windows
mkdir logs

# macOS/Linux
mkdir -p logs
chmod 755 logs
```

## Post-Installation

### Verify Installation

1. **Check database:**

```bash
python manage.py dbshell
> .tables  # Should show auth_*, blog_*, django_* tables
> exit
```

2. **Test API:**

```bash
# In Python shell
python manage.py shell
>>> from blog.models import Message, Conversation
>>> Conversation.objects.count()  # Should be 0 initially
>>> exit()
```

3. **Run tests:**

```bash
python manage.py test blog
```

### Configuration Files to Review

- `my_project/settings.py` - Main project settings
- `blog/config.py` - Bot-specific configuration
- `blog/views.py` - API endpoints and bot logic
- `blog/models.py` - Database models

### Initial Tasks

1. Update `SECRET_KEY` in `settings.py` for production
2. Configure `ALLOWED_HOSTS` appropriately
3. Set up SSL/HTTPS for production
4. Create database backups strategy
5. Review logging configuration in `settings.py`

## Next Steps

After successful installation:

1. **Explore the Admin Interface**
   - Add custom bot responses
   - Review conversation history
   - Analyze user feedback

2. **Customize the UI**
   - Edit `blog/static/style.css` for styling
   - Modify `blog/templates/index.html` for layout

3. **Extend Bot Logic**
   - Add new response patterns in `blog/views.py`
   - Create management commands for automation

4. **Set up Logging**
   - Monitor `logs/django.log` for errors
   - Configure log rotation in `settings.py`

5. **Deploy to Production**
   - Use Gunicorn/uWSGI as application server
   - Set up Nginx as reverse proxy
   - Use PostgreSQL instead of SQLite
   - Enable HTTPS/SSL
   - Set `DEBUG = False`

## Support

For issues or questions:

1. Check the main [README.md](README.md)
2. Review Django documentation: https://docs.djangoproject.com/
3. Check error messages in logs
4. Review troubleshooting section above

## Security Checklist for Production

- [ ] Change `SECRET_KEY`
- [ ] Set `DEBUG = False`
- [ ] Set appropriate `ALLOWED_HOSTS`
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/SSL
- [ ] Set `SESSION_COOKIE_SECURE = True`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up proper database backups
- [ ] Configure firewall rules
- [ ] Use strong admin credentials
- [ ] Set up monitoring and alerting
- [ ] Regular security updates
