"""Management command to load initial bot responses"""
from django.core.management.base import BaseCommand
from blog.models import BotResponse


class Command(BaseCommand):
    help = 'Load initial bot responses into the database'

    def handle(self, *args, **options):
        responses = [
            {
                'keyword': 'hello|hi|hey|greetings',
                'response': 'Hello! How can I help you today?',
                'category': 'greetings',
                'priority': 100,
            },
            {
                'keyword': 'bye|goodbye|farewell|exit',
                'response': 'Goodbye! Have a great day!',
                'category': 'farewell',
                'priority': 100,
            },
            {
                'keyword': 'who are you|what are you|your name|about yourself',
                'response': 'I\'m an intelligent chatbot created with Django. I\'m here to assist you with various tasks!',
                'category': 'identity',
                'priority': 90,
            },
            {
                'keyword': 'help|assist|support|how can|what can',
                'response': 'I can help with greetings, answer questions, provide information about Django, and have general conversations. Feel free to ask!',
                'category': 'help',
                'priority': 90,
            },
            {
                'keyword': 'time|date|current|what time',
                'response': 'I can tell you the current time, but you may need to check your system for exact timezone information.',
                'category': 'time',
                'priority': 80,
            },
            {
                'keyword': 'django|web|framework|python',
                'response': 'Django is a powerful and popular Python web framework for building web applications. Would you like to know more about it?',
                'category': 'tech',
                'priority': 85,
            },
            {
                'keyword': 'weather|temperature|climate',
                'response': 'I don\'t have access to weather data, but you can check weather.com or your local weather service for that information.',
                'category': 'info',
                'priority': 70,
            },
            {
                'keyword': 'thanks|thank you|appreciate|grateful',
                'response': 'You\'re welcome! Happy to help!',
                'category': 'gratitude',
                'priority': 100,
            },
        ]

        created_count = 0
        for response_data in responses:
            response, created = BotResponse.objects.get_or_create(
                keyword=response_data['keyword'],
                defaults={
                    'response': response_data['response'],
                    'category': response_data['category'],
                    'priority': response_data['priority'],
                    'is_active': True,
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created response for: {response_data["keyword"]}')
                )
            else:
                self.stdout.write(f'→ Already exists: {response_data["keyword"]}')

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Successfully loaded {created_count} new bot responses!')
        )
