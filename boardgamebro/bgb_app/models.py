from django.db import models
from django.utils.functional import cached_property
from django.utils import timezone


# Create your models here.
class Game(models.Model):
    """A game to be played and/or owned"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    """Someone who plays games"""
    name = models.CharField(max_length=255)
    games = models.ManyToManyField(Game)

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
        # TODO:
        pass

    def get_most_played_player(self):
        # TODO:
        pass

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

    def __str__(self):
        return f'[{self.date}] {self.game} -> {self.winner}'


class Score(models.Model):
    """Record the score of a *play*. Either one for the final score, or one for each round."""
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    round = models.IntegerField()
    score = models.IntegerField()
