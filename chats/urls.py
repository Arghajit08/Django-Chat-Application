from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns=[
    path('', home, name='home'),
    path('chat/<room_code>/', chat, name='chat'),
]