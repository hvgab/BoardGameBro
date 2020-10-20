from rest_framework import serializers
from django.contrib.auth import models as auth_models
from .. import models


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class GamenightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gamenight
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'


class PlaythroughSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Playthrough
        fields = '__all__'


class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Player
        fields = ['url', 'id', 'nickname']

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    friends = FriendSerializer(many=True)

    class Meta:
        model = models.Player
        fields = ['url', 'id', 'created_at', 'nickname', 'friends']

    def update(self, validated_data):
        pass
        # TODO: GET should return FriendSerializer, but put and patch should just use pk as update value.


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Score
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth_models.User
        fields = [
            'url', 'username', 'first_name', 'last_name', 'date_joined',
            'is_staff', 'player_set'
        ]


# class FriendshipSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Friendship
#         fields = '__all__'
