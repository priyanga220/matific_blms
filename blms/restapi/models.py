from django.db import models

# Create your models here.
class Team(models.Model):
    teamName:models.CharField(max_length=100)
    teamSlogan:models.CharField(max_length=200)
    updatedDate:models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.teamName} ~ {self.teamSlogan}'