from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_response/', views.get_response, name='get_response'),
    path('api/history/', views.conversation_history, name='conversation_history'),
    path('api/feedback/', views.submit_feedback, name='submit_feedback'),
    path('api/statistics/', views.chat_statistics, name='chat_statistics'),
]