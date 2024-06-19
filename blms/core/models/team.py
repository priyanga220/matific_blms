from django.db import models


# Entity mapping for Teams
class Team(models.Model):
    name = models.CharField(max_length=100)
    displayname = models.CharField(max_length=5)
    slogan = models.CharField(max_length=200, null=True)
    rank = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
