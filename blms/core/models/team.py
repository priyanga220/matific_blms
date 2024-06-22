from django.db import models
from .coach import Coach


# Entity mapping for Teams
class Team(models.Model):
    name = models.CharField(max_length=100)
    displayname = models.CharField(max_length=5)
    slogan = models.CharField(max_length=200, null=True)
    rank = models.IntegerField(null=True)
    coach = models.OneToOneField(
        Coach, on_delete=models.PROTECT, related_name="team", null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
