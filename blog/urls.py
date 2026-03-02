from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('specific/',views.specific,name='specific'),
    path('get_response/',views.get_response,name='get_response'),



    # path('article/<int:article_id>/', views.article_detail, name='article_detail'),  ##(article/<int:article_id>/) this allow to pass the number in the urls
]