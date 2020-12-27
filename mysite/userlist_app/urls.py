from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('add_user/', views.add_user, name='add_user'),
    path('chat_box/', views.chat_box, name='chat_box'),
]