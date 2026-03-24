from django.shortcuts import render,HttpResponse
from .models import Message
# Create your views here.

def get_bot_response(message):
    message = message.lower().strip()
    if not message:
        return "Please type something!"
    if 'hello' in message or 'hi' in message:
        return "Hello! How can I help you today?"
    elif 'bye' in message or 'goodbye' in message:
        return "Goodbye! Have a great day!"
    elif 'name' in message:
        return "I'm a simple chatbot created with Django."
    elif 'help' in message:
        return "I can respond to greetings, tell you my name, or say goodbye. Try saying 'hello'!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

def index(request):
    return render(request, 'index.html')

def get_response(request):
    user_message = request.GET.get('userMessage', '')
    response = get_bot_response(user_message)
    # Save to database
    Message.objects.create(user_message=user_message, bot_response=response)
    return HttpResponse(response)


