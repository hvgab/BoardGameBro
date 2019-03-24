from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User
from ..models import Player


class FriendSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'id', 'nickname']


class PlayerSerializer(HyperlinkedModelSerializer):
    friends = FriendSerializer(many=True)

    class Meta:
        model = Player
        fields = ['url', 'id', 'created_at', 'nickname', 'user', 'friends']

    def update(self, validated_data):
        pass
        # TODO: GET should return FriendSerializer, but put and patch should just use pk as update value.


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'username', 'first_name', 'last_name', 'date_joined',
            'is_staff', 'player_set'
        ]


# class FriendshipSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Friendship
#         fields = '__all__'
