from django.db import models
from .player import Player
from .game import Game


# Entity mapping for Playerstats per game
class PlayerStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    impact_index = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.display_name
