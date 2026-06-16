"""Configuration settings for the chatbot"""

# Bot Configuration
BOT_CONFIG = {
    'name': 'AI Assistant',
    'version': '1.0.0',
    'max_conversation_length': 100,  # Maximum messages per conversation
    'session_timeout': 3600,  # Session timeout in seconds (1 hour)
    'confidence_threshold': 0.3,  # Minimum confidence to use response
    'enable_logging': True,
    'enable_feedback': True,
}

# Response Categories
RESPONSE_CATEGORIES = {
    'greetings': 'Greeting Responses',
    'farewell': 'Farewell Responses',
    'identity': 'Identity Questions',
    'help': 'Help Requests',
    'time': 'Time/Date Requests',
    'tech': 'Technical Questions',
    'info': 'General Information',
    'gratitude': 'Gratitude Expressions',
    'general': 'General Responses',
}

# Response Patterns with priority
RESPONSE_PATTERNS = {
    'greetings': {
        'keywords': ['hello', 'hi', 'hey', 'greetings', 'howdy', 'what\'s up'],
        'priority': 100,
    },
    'farewell': {
        'keywords': ['bye', 'goodbye', 'farewell', 'see you', 'take care', 'exit'],
        'priority': 100,
    },
    'identity': {
        'keywords': ['who are you', 'what are you', 'your name', 'about yourself'],
        'priority': 90,
    },
    'help': {
        'keywords': ['help', 'assist', 'support', 'how can', 'what can'],
        'priority': 85,
    },
}

# UI Configuration
UI_CONFIG = {
    'theme': 'light',
    'enable_dark_mode': False,
    'chat_width_desktop': 500,
    'chat_width_mobile': '100%',
    'message_animation': True,
    'show_timestamps': True,
    'show_confidence': True,
}

# API Configuration
API_CONFIG = {
    'rate_limit': 100,  # Requests per minute
    'timeout': 30,  # Request timeout in seconds
    'max_message_length': 1000,
    'response_format': 'json',
}
