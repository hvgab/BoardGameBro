from django.db import models
from django.db.models import Count
from django.utils.functional import cached_property
from django.utils import timezone
from .play import Play
from .player import Player


class Score(models.Model):
    """Record the score of a *play*. Either one for the final score, or one for each round."""
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    round = models.IntegerField()
    score = models.IntegerField()
