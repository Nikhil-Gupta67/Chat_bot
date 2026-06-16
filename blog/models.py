from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Conversation(models.Model):
    """Store conversation sessions"""
    session_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Conversation {self.session_id} - {self.created_at}"

class Message(models.Model):
    """Store individual messages in conversations"""
    MESSAGE_TYPE_CHOICES = [
        ('user', 'User Message'),
        ('bot', 'Bot Response'),
    ]
    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    user_message = models.TextField()
    bot_response = models.TextField()
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES, default='user')
    confidence_score = models.FloatField(default=0.0, help_text="Bot response confidence (0-1)")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_helpful = models.BooleanField(null=True, blank=True, help_text="User feedback on response")
    
    class Meta:
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['conversation', 'timestamp']),
        ]
    
    def __str__(self):
        return f"Msg: {self.user_message[:40]}... | Response: {self.bot_response[:40]}..."

class BotResponse(models.Model):
    """Store predefined bot responses for easy management"""
    keyword = models.CharField(max_length=200)
    response = models.TextField()
    category = models.CharField(max_length=50, default='general')
    priority = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    usage_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-priority', '-usage_count']
    
    def __str__(self):
        return f"{self.keyword} - {self.response[:50]}..."

class ChatFeedback(models.Model):
    """Store user feedback on bot responses"""
    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Feedback: {self.rating}/5 - {self.message.user_message[:30]}..."
