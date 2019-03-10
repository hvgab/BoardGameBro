from django.db import models
from django.utils import timezone


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_winrate(self):
        wins = self.play_set.filter(winner=self).count()
        plays = self.play_set.count()
        winrate = wins / plays
        print(f'wins: {wins}')
        print(f'plays: {plays}')
        print(f'winrate: {winrate}')
        print(f'winrate: {type(winrate)}')
        return winrate

    def get_most_played_game(self):
        # TODO:
        pass

    def get_most_played_player(self):
        # TODO:
        pass


class Play(models.Model):
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
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    round = models.IntegerField()
    score = models.IntegerField()
