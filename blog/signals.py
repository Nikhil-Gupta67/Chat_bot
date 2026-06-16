"""Signal handlers for the blog app"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Message, BotResponse
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Message)
def log_message_created(sender, instance, created, **kwargs):
    """Log when a message is created"""
    if created:
        logger.info(f"New message created: {instance.id} with confidence: {instance.confidence_score}")


@receiver(post_save, sender=BotResponse)
def log_bot_response_created(sender, instance, created, **kwargs):
    """Log when a bot response is created or updated"""
    if created:
        logger.info(f"New bot response created: {instance.keyword}")
    else:
        logger.info(f"Bot response updated: {instance.keyword}")
