from django.db import models
from .team import Team


# Entity mapping for Players
class Player(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    rank = models.IntegerField(null=True)
    height = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.display_name
