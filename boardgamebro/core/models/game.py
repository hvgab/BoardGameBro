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
