"""Context processors for blog app"""
from .config import BOT_CONFIG, UI_CONFIG
import logging

logger = logging.getLogger(__name__)


def bot_settings(request):
    """Add bot settings to template context"""
    return {
        'bot_name': BOT_CONFIG.get('name', 'Bot'),
        'bot_version': BOT_CONFIG.get('version', '1.0.0'),
        'ui_config': UI_CONFIG,
    }
