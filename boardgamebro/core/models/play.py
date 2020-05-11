from django.db import models
from django.db.models import Count
from django.utils.functional import cached_property
from django.utils import timezone
from .game import Game
from .player import Player
from django.contrib.auth.models import User
from django.urls import reverse


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
        return ', '.join(p.nickname for p in self.players.all())

    @property
    def final_scores(self):
        pass

    def __str__(self):
        return f'[{self.date}] {self.game} -> {self.winner}'

    def get_absolute_url(self):
        return reverse('bgb:play-detail', kwargs={'pk': self.id})
