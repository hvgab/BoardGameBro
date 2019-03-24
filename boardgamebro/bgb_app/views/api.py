from rest_framework import viewsets
from django.contrib.auth.models import User
from ..models import Player
from ..serializers import UserSerializer, PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """    API endpoint ...    """
    queryset = Player.objects.filter(
        is_deleted=False).all().order_by('-created_at')
    serializer_class = PlayerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """    API endpoint ...    """
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
