from django.db import models


# Entity mapping for Tournaments
class Tournament(models.Model):
    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    mascot = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.identifier
