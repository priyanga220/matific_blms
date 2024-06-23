from core.models import UserStat
from django.db.models import Sum, Count, F
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404
from datetime import datetime


class UserService:
    def addUserLoginStat(self, user):
        print(user.pk)
        existing = UserStat.objects.filter(user__id=user.pk, logout_at__isnull=True)
        if existing:
            for stat in existing:
                stat.logout_at = datetime.now()
                stat.save()

        userstat: UserStat = UserStat(login_at=datetime.now, user=user)
        userstat.save()

    def setUserLogoutStat(self, user):
        userStat: UserStat = (
            UserStat.objects.filter(user__id=user.pk, logout_at__isnull=True)
            .order_by("-login_at")
            .first()
        )

        if userStat:
            userStat.logout_at = datetime.now()
            userStat.save()

    def loadUserstats(self):
        # samples = UserStat.objects.values("user__id").annotate(
        #    aliquots=Count("user__id"), times=F("logout_at") - F("login_at")
        # )
        samples = (
            UserStat.objects.all()
            .values(
                "user__id",
                "user__first_name",
                "user__last_name",
                "user__username",
                "user__userrole",
            )
            .annotate(
                totallogins=Count("user__id"),
                totaltime=Sum(F("logout_at") - F("login_at")),
            )
            .order_by("totallogins")
        )
        return samples

    def loadOnlineUsers(self):
        return [token.user for token in Token.objects.all()]

    def get_object(self, pk: int) -> UserStat:
        try:
            return UserStat.objects.get(pk=pk)
        except UserStat.DoesNotExist:
            raise Http404

    def convert_timedelta(duration):
        days, seconds = duration.days, duration.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return hours, minutes, seconds
