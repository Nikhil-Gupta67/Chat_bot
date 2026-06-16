from django import forms
from .models import Message, ChatFeedback

class ChatMessageForm(forms.ModelForm):
    """Form for submitting chat messages"""
    class Meta:
        model = Message
        fields = ['user_message', 'bot_response']
        widgets = {
            'user_message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message here...',
                'id': 'userMessage'
            }),
            'bot_response': forms.Textarea(attrs={
                'class': 'form-control',
                'readonly': True
            }),
        }

class ChatFeedbackForm(forms.ModelForm):
    """Form for submitting feedback on chat responses"""
    class Meta:
        model = ChatFeedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=ChatFeedback._meta.get_field('rating').choices),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional: Share your feedback...',
                'rows': 3
            }),
        }
