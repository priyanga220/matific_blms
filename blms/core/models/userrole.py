from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class UserRole(models.Model):

    # Fields for ROLES
    ADMIN = 0
    COACH = 1
    PLAYER = 2

    ROLE_CHOICES = ((ADMIN, "Admin"), (COACH, "Coach"), (PLAYER, "Player"))

    # Fields for generic relation on User type (Coach / Player or Admin) based on role
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    userrole = models.IntegerField(max_length=2, choices=ROLE_CHOICES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.user.normalize_username} - {self.userrole}")

    class Meta:
        unique_together = ("content_type", "object_id")
