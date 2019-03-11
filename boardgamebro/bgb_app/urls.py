from django.urls import path
from .views import *

app_name = 'bgb'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # PLAYER
    path('players/', PlayerListView.as_view(), name='player-list'),
    path(
        'players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    # PLAY
    path('plays/', PlayListView.as_view(), name='play-list'),
    path('plays/<int:pk>/', PlayDetailView.as_view(), name='play-detail'),
    path('plays/new', PlayCreateView.as_view(), name='play-new'),
    # GAME
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]
