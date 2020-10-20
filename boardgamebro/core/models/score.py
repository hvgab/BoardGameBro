from django.db import models
from django.db.models import Count
from django.utils.functional import cached_property
from django.utils import timezone
from .playthrough import Playthrough
from .player import Player


class Score(models.Model):
    """Record the score of a playthrough. Either one for the final score, or one for each round."""

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
        constraints = [
            models.UniqueConstraint(fields=['playthrough', 'player', 'round'], name='unique_round_score')
        ]

    playthrough = models.ForeignKey('Playthrough', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    round = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return f'{self.playthrough.name}, {self.player.nickname}. {self.round}:{self.score}'