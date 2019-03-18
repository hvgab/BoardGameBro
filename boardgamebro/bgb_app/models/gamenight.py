from django.db import models
from .player import Player
from .location import Location
from django.utils import timezone


class Gamenight(models.Model):
    """If the user creates a gamenight, new play-records will auto-fill with gamenight-players and gamenight-date"""
    name = models.CharField(
        max_length=30
    )  # kan jeg sette default til en funksjon som returnerer en string?
    description = models.TextField(
        verbose_name='Describe the gamenight', null=True, blank=True)
    host = models.ForeignKey(
        Player, on_delete=models.SET_NULL, null=True, related_name='host_of')
    date = models.DateField(
        verbose_name='gamenight was held at', default=timezone.now)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField(Player)

    def set_gamenight_default(self):
        return ','.join([player.nickname for player in self.players.all])
