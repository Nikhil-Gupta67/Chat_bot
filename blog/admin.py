from django.contrib import admin
from .models import Message, Conversation, BotResponse, ChatFeedback

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'user', 'created_at', 'updated_at', 'is_active', 'message_count')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('session_id', 'user__username')
    readonly_fields = ('session_id', 'created_at', 'updated_at')
    
    def message_count(self, obj):
        return obj.messages.count()
    message_count.short_description = 'Total Messages'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'user_message_preview', 'bot_response_preview', 'confidence_score', 'timestamp', 'is_helpful')
    list_filter = ('message_type', 'is_helpful', 'confidence_score', 'timestamp')
    search_fields = ('user_message', 'bot_response')
    readonly_fields = ('timestamp', 'message_preview')
    date_hierarchy = 'timestamp'
    
    def user_message_preview(self, obj):
        return obj.user_message[:50] + '...' if len(obj.user_message) > 50 else obj.user_message
    user_message_preview.short_description = 'User Message'
    
    def bot_response_preview(self, obj):
        return obj.bot_response[:50] + '...' if len(obj.bot_response) > 50 else obj.bot_response
    bot_response_preview.short_description = 'Bot Response'
    
    def message_preview(self, obj):
        return f"User: {obj.user_message}\\n\\nBot: {obj.bot_response}"
    message_preview.short_description = 'Full Message'

@admin.register(BotResponse)
class BotResponseAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'category', 'priority', 'is_active', 'usage_count', 'created_at')
    list_filter = ('category', 'is_active', 'priority')
    search_fields = ('keyword', 'response')
    readonly_fields = ('usage_count', 'created_at')
    fieldsets = (
        ('Basic Info', {'fields': ('keyword', 'response', 'category')}),
        ('Management', {'fields': ('priority', 'is_active')}),
        ('Statistics', {'fields': ('usage_count', 'created_at')}),
    )

@admin.register(ChatFeedback)
class ChatFeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'rating', 'comment_preview', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('message__user_message', 'comment')
    readonly_fields = ('created_at', 'message')
    
    def comment_preview(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = 'Comment'
