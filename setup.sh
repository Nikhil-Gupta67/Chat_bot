#!/bin/bash
# Setup script for Django Chatbot Application (macOS/Linux)

echo "========================================"
echo "Django Chatbot Setup Script"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed or not in PATH"
    exit 1
fi

echo "[OK] Python 3 found"
echo

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to create virtual environment"
    exit 1
fi
echo "[OK] Virtual environment created"
echo

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate
echo "[OK] Virtual environment activated"
echo

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi
echo "[OK] Dependencies installed"
echo

# Run migrations
echo "Running database migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to run migrations"
    exit 1
fi
echo "[OK] Database migrations completed"
echo

# Load initial bot responses
echo "Loading initial bot responses..."
python manage.py load_bot_responses
echo "[OK] Initial bot responses loaded"
echo

# Create superuser
echo
echo "========================================"
echo "Create Admin User (Superuser)"
echo "========================================"
echo
python manage.py createsuperuser

echo
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo
echo "To run the server, execute:"
echo "  source .venv/bin/activate"
echo "  python manage.py runserver"
echo
echo "Then open:"
echo "  http://127.0.0.1:8000/"
echo
