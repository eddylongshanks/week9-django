from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_box, name='chat_box'),
    path('test/', views.test, name='test'),
    path('user_list/', views.user_list, name='user_list'),
    path('add_user/', views.add_user, name='add_user'),
]