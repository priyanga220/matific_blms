from django.db import models
from .team import Team
from .game import Game
from .player import Player


# Entity mapping for Gamestats including teams data,  per match 2 entries
class GameStat(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="teamstats"
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="gamestats")
    teamref = models.CharField(max_length=100)
    score = models.IntegerField(null=True)
    iswinner = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.teamref} - [{self.game}]"
