from django.db import models
from .team import Team


# Entity mapping for Coaches
class Coach(models.Model):
    name = models.CharField(max_length=200)
    team = models.OneToOneField(Team, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
