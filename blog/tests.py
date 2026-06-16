from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Message, Conversation, BotResponse, ChatFeedback
from .views import get_bot_response
import json

class BotResponseTestCase(TestCase):
    """Test bot response generation logic"""
    
    def test_greeting_response(self):
        """Test greeting responses"""
        response, confidence = get_bot_response('hello')
        self.assertEqual(response, "Hello! How can I help you today?")
        self.assertGreater(confidence, 0.9)
    
    def test_farewell_response(self):
        """Test farewell responses"""
        response, confidence = get_bot_response('bye')
        self.assertEqual(response, "Goodbye! Have a great day!")
        self.assertGreater(confidence, 0.9)
    
    def test_identity_response(self):
        """Test identity question responses"""
        response, confidence = get_bot_response('who are you')
        self.assertIn('intelligent chatbot', response.lower())
        self.assertGreater(confidence, 0.8)
    
    def test_help_response(self):
        """Test help request responses"""
        response, confidence = get_bot_response('help')
        self.assertIn('assist', response.lower())
        self.assertGreater(confidence, 0.8)
    
    def test_empty_message(self):
        """Test empty message handling"""
        response, confidence = get_bot_response('')
        self.assertEqual(response, "Please type something!")
        self.assertGreater(confidence, 0.4)
    
    def test_unknown_response(self):
        """Test response to unknown message"""
        response, confidence = get_bot_response('xyzabc12345')
        self.assertIn('understand', response.lower())
        self.assertLess(confidence, 0.5)
    
    def test_case_insensitivity(self):
        """Test case-insensitive responses"""
        response1, _ = get_bot_response('HELLO')
        response2, _ = get_bot_response('hello')
        self.assertEqual(response1, response2)

class ConversationModelTestCase(TestCase):
    """Test Conversation model"""
    
    def setUp(self):
        self.conversation = Conversation.objects.create(session_id='test-session-123')
    
    def test_conversation_creation(self):
        """Test conversation creation"""
        self.assertIsNotNone(self.conversation.id)
        self.assertEqual(self.conversation.session_id, 'test-session-123')
        self.assertTrue(self.conversation.is_active)
    
    def test_conversation_string_representation(self):
        """Test conversation string representation"""
        self.assertIn('test-session-123', str(self.conversation))

class MessageModelTestCase(TestCase):
    """Test Message model"""
    
    def setUp(self):
        self.conversation = Conversation.objects.create(session_id='test-session-456')
        self.message = Message.objects.create(
            conversation=self.conversation,
            user_message='Hello',
            bot_response='Hi there!',
            confidence_score=0.95
        )
    
    def test_message_creation(self):
        """Test message creation"""
        self.assertIsNotNone(self.message.id)
        self.assertEqual(self.message.user_message, 'Hello')
        self.assertEqual(self.message.bot_response, 'Hi there!')
        self.assertEqual(self.message.confidence_score, 0.95)
    
    def test_message_timestamp(self):
        """Test message timestamp is set"""
        self.assertIsNotNone(self.message.timestamp)
    
    def test_message_conversation_relationship(self):
        """Test message-conversation relationship"""
        self.assertEqual(self.message.conversation, self.conversation)
        self.assertEqual(self.conversation.messages.count(), 1)

class ChatViewsTestCase(TestCase):
    """Test chat views and API endpoints"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='123456')
    
    def test_index_view(self):
        """Test index view returns HTML"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_response_endpoint(self):
        """Test get_response API endpoint"""
        response = self.client.get('/get_response/', {'userMessage': 'hello'})
        self.assertEqual(response.status_code, 200)
    
    def test_get_response_empty_message(self):
        """Test get_response with empty message"""
        response = self.client.get('/get_response/', {'userMessage': ''})
        self.assertEqual(response.status_code, 400)
    
    def test_conversation_history_endpoint(self):
        """Test conversation history API"""
        # Create a conversation with messages
        self.client.get('/get_response/', {'userMessage': 'hello'})
        response = self.client.get('/api/history/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertGreater(data['message_count'], 0)
    
    def test_statistics_endpoint(self):
        """Test statistics API"""
        self.client.get('/get_response/', {'userMessage': 'hello'})
        response = self.client.get('/api/statistics/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertIn('total_messages', data)
        self.assertIn('avg_confidence', data)
