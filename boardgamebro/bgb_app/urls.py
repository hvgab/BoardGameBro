from django.urls import path
from .views import *

app_name = 'bgb'

urlpatterns = [
    # BGB APP
    path('', HomeView.as_view(), name='home'),
    path('about/', HomeView.as_view(), name='home'),
    path('about/tos', HomeView.as_view(), name='home'),
    path('about/privacy', HomeView.as_view(), name='home'),

    # ACCOUNT
    path('accounts/profile/', Profile.as_view(), name='profile'),

    ## PLAYER
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/', PlayerCreateView.as_view(), name='player-create'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('players/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),
    
    ## PLAY
    path('plays/', PlayListView.as_view(), name='play-list'),
    path('plays/', PlayCreateView.as_view(), name='play-create'),
    path('plays/<int:pk>/', PlayDetailView.as_view(), name='play-detail'),
    path('plays/<int:pk>/update', PlayUpdateView.as_view(), name='play-update'),
    path('plays/<int:pk>/delete', PlayDeleteView.as_view(), name='play-delete'),
    
    ## GAME
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/', GameCreateView.as_view(), name='game-create'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('games/<int:pk>/update/', GameUpdateView.as_view(), name='game-update'),
    path('games/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),
]
