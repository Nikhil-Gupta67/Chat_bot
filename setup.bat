@echo off
REM Setup script for Django Chatbot Application (Windows)

echo ========================================
echo Django Chatbot Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv .venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment created
echo.

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo [OK] Virtual environment activated
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

REM Run migrations
echo Running database migrations...
python manage.py migrate
if errorlevel 1 (
    echo [ERROR] Failed to run migrations
    pause
    exit /b 1
)
echo [OK] Database migrations completed
echo.

REM Load initial bot responses
echo Loading initial bot responses...
python manage.py load_bot_responses
echo [OK] Initial bot responses loaded
echo.

REM Create superuser
echo.
echo ========================================
echo Create Admin User (Superuser)
echo ========================================
echo.
python manage.py createsuperuser

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the server, execute:
echo   .venv\Scripts\activate
echo   python manage.py runserver
echo.
echo Then open:
echo   http://127.0.0.1:8000/
echo.
pause
