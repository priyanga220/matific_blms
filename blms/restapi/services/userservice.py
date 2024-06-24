from core.models import UserStat
from django.db.models import Sum, Count, F
from rest_framework.authtoken.models import Token
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

    # Return user stats with total logins and total login time for users
    # totoallogin - count the userstat entries group by userid
    # totaltime - Sum the deference of (logout_at - login_at) deltas group by user_id
    # needs further enhancements on this logic if no logout_at it defaults to current time etc
    def loadUserstats(self):
        userstats = (
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
        return userstats

    def loadOnlineUsers(self):
        return [token.user for token in Token.objects.all()]

    def get_object(self, pk: int) -> UserStat:
        try:
            return UserStat.objects.get(pk=pk)
        except UserStat.DoesNotExist:
            raise Http404
