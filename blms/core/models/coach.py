from django.db import models


# Entity mapping for Coaches
class Coach(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
