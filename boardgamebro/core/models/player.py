from django.db import models
from django.db.models import Count
from django.utils.functional import cached_property
from django.utils import timezone
from .game import Game
from django.contrib.auth.models import User

# class Friendship(models.Model):
#     player = models.ForeignKey(
#         'Player', on_delete=models.CASCADE, related_name='player')
#     friend = models.ForeignKey(
#         'Player', on_delete=models.CASCADE, related_name='friend')
#     friends_since = models.DateTimeField(verbose_name='Became friends at')


class Player(models.Model):
    """Someone who plays games"""
    # PROFILE STUFF
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='creator_of')
    is_deleted = models.BooleanField(default=False, verbose_name='player is deleted')
    deleted_at = models.DateTimeField(verbose_name='player was deleted at', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email_communication = models.BooleanField(default=False, null=True, blank=True, verbose_name='Would you like to get awesome news from us?') # GDPR Opt-IN

    # PLAYER STUFF
    nickname = models.CharField(max_length=255)
    games = models.ManyToManyField(Game, blank=True, verbose_name='Games owned')
    friends = models.ManyToManyField('self', blank=True)

    @cached_property
    def win_count(self):
        return self.play_set.filter(winner=self).count()

    @cached_property
    def play_count(self):
        return self.play_set.count()

    @cached_property
    def game_count(self):
        return self.games.count()

    @property
    def winrate(self):
        try:
            return self.win_count / self.play_count
        except:
            return 0

    @property
    def winpercent(self):
        return f'{self.winrate*100}'

    def get_most_played_game(self):
        game_total = self.play_set.values('game').annotate(
            total=Count('game')).order_by('-total').first()
        game = Game.objects.get(id=game_total['game'])
        return game

    def get_winpercent(self, game: 'Game' = None, player: 'Player' = None):
        """Get winpercent *either* game *or* player"""
        if game and player:
            pass
        elif game:
            play_count = self.play_set.filter(game=game).count()
            win_count = self.play_set.filter(winner=self, game=game).count()
            return win_count / play_count * 100
        elif player:
            pass
            # play_count = self.play_set.filter(players__in=player).count()
            # win_count = self.play_set.filter(
            #     winner=self, player=player).count()
            # return win_count / play_count * 100
        else:
            return self.winpercent

    def get_played_agains_count(self):
        my_plays = self.play_set.all()
        my_plays_ids = [x.id for x in my_plays]
        players_with_count = Play.players.through.objects.filter(
            play_id__in=my_plays_ids).values('player_id').annotate(
                count=Count('player_id')).all()
        return players_with_count
        # {'player_id: 1, 'count': 3}
        # etc

    def get_most_played_player(self):
        from .play import Play
        my_plays = self.play_set.all()
        my_plays_ids = [x.id for x in my_plays]

        most_played_player_id = Play.players.through.objects.filter(
            play_id__in=my_plays_ids).exclude(
                player_id=self.id).values('player_id').annotate(
                    count=Count('player_id')).order_by('-count').first()

        opponent = Player.objects.get(id=most_played_player_id['player_id'])
        return opponent

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'Player({self.nickname})'
