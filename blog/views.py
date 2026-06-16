from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db import models
import json
import uuid
from .models import Message, Conversation, BotResponse, ChatFeedback
import logging

logger = logging.getLogger(__name__)

# Enhanced bot response logic with pattern matching
def get_bot_response(message):
    """Generate bot response with enhanced NLP logic"""
    message = message.lower().strip()
    confidence = 0.0
    
    if not message:
        return "Please type something!", 0.5
    
    # Greeting patterns
    greetings = ['hello', 'hi', 'hey', 'greetings', 'howdy', 'what\'s up']
    if any(greeting in message for greeting in greetings):
        return "Hello! How can I help you today?", 0.95
    
    # Farewell patterns
    farewells = ['bye', 'goodbye', 'farewell', 'see you', 'take care', 'exit']
    if any(farewell in message for farewell in farewells):
        return "Goodbye! Have a great day!", 0.95
    
    # Identity patterns
    identity_keywords = ['who are you', 'what are you', 'your name', 'about yourself']
    if any(keyword in message for keyword in identity_keywords):
        return "I'm an intelligent chatbot created with Django. I'm here to assist you!", 0.90
    
    # Help patterns
    help_keywords = ['help', 'assist', 'support', 'how can', 'what can']
    if any(keyword in message for keyword in help_keywords):
        return "I can help with greetings, answer questions, and provide general assistance. Feel free to ask!", 0.85
    
    # Time/Date patterns
    time_keywords = ['time', 'date', 'current', 'what time', 'what\'s the time']
    if any(keyword in message for keyword in time_keywords):
        from django.utils import timezone
        current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current time is: {current_time}", 0.90
    
    # Django-related questions
    django_keywords = ['django', 'web', 'framework', 'python']
    if any(keyword in message for keyword in django_keywords):
        return "Django is a powerful Python web framework! I was built with it. Is there anything specific you'd like to know?", 0.80
    
    # Weather-like requests
    if 'weather' in message or 'temperature' in message:
        return "I don't have access to weather data, but you can check weather.com for that information!", 0.75
    
    # Gratitude responses
    gratitude = ['thanks', 'thank you', 'appreciate', 'grateful']
    if any(g in message for g in gratitude):
        return "You're welcome! Happy to help!", 0.90
    
    # Fallback response
    return "I'm sorry, I didn't understand that. Can you rephrase? Feel free to ask for 'help' for more options.", 0.40

def get_or_create_conversation(request):
    """Get or create conversation session"""
    session_id = request.session.get('conversation_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['conversation_id'] = session_id
    
    conversation, created = Conversation.objects.get_or_create(
        session_id=session_id,
        defaults={'user': request.user if request.user.is_authenticated else None}
    )
    return conversation

def index(request):
    """Main chat interface"""
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def get_response(request):
    """API endpoint for bot responses - supports both GET and POST"""
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user_message = data.get('userMessage', '').strip()
        else:
            user_message = request.GET.get('userMessage', '').strip()
        
        if not user_message:
            return JsonResponse({
                'success': False,
                'error': 'Message cannot be empty',
                'message': 'Please type something!'
            }, status=400)
        
        # Get or create conversation
        conversation = get_or_create_conversation(request)
        
        # Get bot response
        bot_response, confidence = get_bot_response(user_message)
        
        # Create and save message
        message = Message.objects.create(
            conversation=conversation,
            user_message=user_message,
            bot_response=bot_response,
            confidence_score=confidence
        )
        
        logger.info(f"Message created: {message.id} with confidence: {confidence}")
        
        # Return JSON response for modern clients, plain text for legacy
        if request.headers.get('Accept') == 'application/json' or request.method == 'POST':
            return JsonResponse({
                'success': True,
                'message': bot_response,
                'confidence': confidence,
                'message_id': message.id,
                'timestamp': message.timestamp.isoformat()
            })
        else:
            return HttpResponse(bot_response)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON format'
        }, status=400)
    except Exception as e:
        logger.error(f"Error in get_response: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'An error occurred',
            'message': 'I encountered an error processing your request.'
        }, status=500)

@require_http_methods(["GET"])
def conversation_history(request):
    """Get conversation history"""
    conversation = get_or_create_conversation(request)
    messages = conversation.messages.all().values('user_message', 'bot_response', 'timestamp', 'confidence_score')
    
    return JsonResponse({
        'success': True,
        'conversation_id': conversation.session_id,
        'message_count': messages.count(),
        'messages': list(messages)
    })

@require_http_methods(["POST"])
def submit_feedback(request):
    """Submit feedback on bot response"""
    try:
        data = json.loads(request.body)
        message_id = data.get('message_id')
        rating = data.get('rating', 3)
        comment = data.get('comment', '')
        
        message = Message.objects.get(id=message_id)
        ChatFeedback.objects.update_or_create(
            message=message,
            defaults={'rating': rating, 'comment': comment}
        )
        
        return JsonResponse({'success': True, 'message': 'Feedback submitted successfully'})
    except Message.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Message not found'}, status=404)
    except Exception as e:
        logger.error(f"Error in submit_feedback: {str(e)}")
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@require_http_methods(["GET"])
def chat_statistics(request):
    """Get chat statistics"""
    conversation = get_or_create_conversation(request)
    messages = conversation.messages.all()
    
    total_messages = messages.count()
    avg_confidence = messages.aggregate(
        models.Avg('confidence_score')
    )['confidence_score__avg'] or 0
    
    feedback_stats = ChatFeedback.objects.filter(
        message__conversation=conversation
    ).aggregate(
        avg_rating=models.Avg('rating'),
        total_feedback=models.Count('id')
    )
    
    return JsonResponse({
        'success': True,
        'total_messages': total_messages,
        'avg_confidence': round(avg_confidence, 2),
        'feedback_count': feedback_stats['total_feedback'],
        'avg_rating': round(feedback_stats['avg_rating'], 2) if feedback_stats['avg_rating'] else 0
    })


