from django.db import models
from django.db.models import Count
from django.utils.functional import cached_property
from django.utils import timezone


# Create your models here.
class Game(models.Model):
    """A game to be played and/or owned"""
    name = models.CharField(max_length=255)

    @property
    def play_count(self):
        return self.play_set.count()

    @property
    def player_count(self):
        return self.player_set.count()

    def __str__(self):
        return self.name


class Player(models.Model):
    """Someone who plays games"""
    name = models.CharField(max_length=255)
    games = models.ManyToManyField(Game, null=True, blank=True)

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
        my_plays = self.play_set.all()
        my_plays_ids = [x.id for x in my_plays]

        most_played_player_id = Play.players.through.objects.filter(
            play_id__in=my_plays_ids).exclude(
                player_id=self.id).values('player_id').annotate(
                    count=Count('player_id')).order_by('-count').first()

        opponent = Player.objects.get(id=most_played_player_id['player_id'])
        return opponent

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Player({self.name})'


class Play(models.Model):
    """Players have played a game"""
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    date = models.DateField(
        default=timezone.now, help_text='When was the game played?')
    game = models.ForeignKey(
        Game,
        on_delete=models.SET_NULL,
        null=True,
        help_text='What game was played?')
    players = models.ManyToManyField(Player, help_text='Who was playing?')
    winner = models.ForeignKey(
        Player, on_delete=models.SET_NULL, null=True, related_name='winner')

    @property
    def players_string(self):
        return ', '.join(p.name for p in self.players.all())

    def __str__(self):
        return f'[{self.date}] {self.game} -> {self.winner}'


class Score(models.Model):
    """Record the score of a *play*. Either one for the final score, or one for each round."""
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    round = models.IntegerField()
    score = models.IntegerField()
