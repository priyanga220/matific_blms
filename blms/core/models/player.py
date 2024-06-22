from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .team import Team
from .userrole import UserRole


# Entity mapping for Players
class Player(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=50)
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, related_name="players", null=True
    )
    rank = models.IntegerField(null=True)
    height = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    userrole = GenericRelation(UserRole)

    @property
    def role(self):
        return self.userrole.first()

    def __str__(self) -> str:
        return str(self.display_name)
