from django.db import models
from enumchoicefield import EnumChoiceField
from .tournament import Tournament
from ..enums import GameType
from ..enums import GameStatus


# Entity mapping for Games
class Game(models.Model):
    game_level = EnumChoiceField(GameType, default=GameType.QU)
    status = EnumChoiceField(GameStatus, default=GameStatus.SC)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{(self.gamestats.all()[0]).teamref} vs {(self.gamestats.all()[1]).teamref}"
