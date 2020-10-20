from django.urls import path
from .views import *
# from .views import api as api_views

app_name = 'bgb'

urlpatterns = [
    path('playthrough_form', PlaythroughForm.as_view(), name='playthrough-form'),
    # path('playthrough_form', PlaythroughForm.as_view(), name='playthrough-form'),

    # BGB APP
    path('', HomeView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),

    # ACCOUNT
    path('accounts/profile/', Profile.as_view(), name='profile'),

    ## PLAYER
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    
    ## PLAY
    path('playthroughs/', PlaythroughListView.as_view(), name='playthrough-list'),
    path('playthroughs/<int:pk>/', PlaythroughDetailView.as_view(), name='playthrough-detail'),
    path('playthroughs/<int:pk>/edit', PlaythroughUpdateView.as_view(), name='playthrough-update'),
    path('playthroughs/create', PlaythroughCreateView.as_view(), name='playthrough-create'),
    
    ## GAME
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]

