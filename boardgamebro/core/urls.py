from django.urls import path
from .views import *
# from .views import api as api_views

app_name = 'bgb'

urlpatterns = [
    path('session_form', SessionForm.as_view(), name='session-form'),

    # BGB APP
    path('', HomeView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),

    # ACCOUNT
    path('accounts/profile/', Profile.as_view(), name='profile'),

    ## PLAYER
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    
    ## PLAY
    path('plays/', PlayListView.as_view(), name='play-list'),
    path('plays/<int:pk>/', PlayDetailView.as_view(), name='play-detail'),
    path('plays/<int:pk>/edit', PlayUpdateView.as_view(), name='play-update'),
    path('plays/create', PlayCreateView.as_view(), name='play-create'),
    
    ## GAME
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]
