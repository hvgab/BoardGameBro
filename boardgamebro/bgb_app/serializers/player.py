<<<<<<< HEAD
from rest_framework import serializers
from ..models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
=======
from rest_framework.serializers import HyperlinkedModelSerializer
from ..models import Player

# class PlayerSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Player
#         exclude = ['user']
>>>>>>> feature/friends
