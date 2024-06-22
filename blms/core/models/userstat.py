from django.db import models
from django.contrib.auth import get_user_model


# Entity mapping for User Stat data
class UserStat(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_at = models.DateTimeField(auto_now_add=True)
    logout_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"Log in :  {self.login_at}"
