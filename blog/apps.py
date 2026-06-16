from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Chat Bot Application'
    
    def ready(self):
        """Initialize app and set up signal handlers"""
        import blog.signals  # noqa
        logger.info('Blog app initialized successfully')
