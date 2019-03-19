from django.urls import path
from .views import *

app_name = 'bgb'

urlpatterns = [
    # ACCOUNT
    path('accounts/profile/', Profile.as_view(), name='profile'),

    # BGB APP
    path('', HomeView.as_view(), name='home'),
    ## PLAYER
    path('players/', PlayerListView.as_view(), name='player-list'),
    path(
        'players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    ## PLAY
    path('plays/', PlayListView.as_view(), name='play-list'),
    path('plays/<int:pk>/', PlayDetailView.as_view(), name='play-detail'),
    path('plays/create', PlayCreateView.as_view(), name='play-create'),
    ## GAME
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]
