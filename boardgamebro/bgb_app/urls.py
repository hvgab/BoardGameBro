from django.urls import path
from .views import player

app_name = 'bgb'

urlpatterns = [path('player/<int:pk>', player)]
