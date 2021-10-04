from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'wheelspin'

urlpatterns = [ 
    path('reqForROOM/<str:bet>/<str:total>',reqForROOM,name='reqForROOM'),
    path('wheelgame/<str:room_name>/',wheelgame,name='wheelgame'),
    path('<str:room_name>/',room,name='room'),
]