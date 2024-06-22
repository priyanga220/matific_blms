from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from .userrole import UserRole


# Entity mapping for Coaches
class Coach(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    userrole = GenericRelation(UserRole)

    @property
    def role(self):
        return self.userrole.first()

    def __str__(self) -> str:
        return str(self.name)
