from rest_framework import viewsets
from ..models import *
from django.contrib.auth import models as auth_models
from ..serializers import *


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GamenightViewSet(viewsets.ModelViewSet):
    queryset = Gamenight.objects.all()
    serializer_class = GamenightSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """    API endpoint ...    """
    queryset = Player.objects.filter(is_deleted=False).all().order_by('-created_at')
    serializer_class = PlayerSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class UserViewSet(viewsets.ModelViewSet):
    """    API endpoint ...    """
    queryset = auth_models.User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
