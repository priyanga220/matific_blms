from django.urls import path
from rest_framework.authtoken import views

from .views import teamviews
from .views import playerviews
from .views import tournamentviews
from .views import coachviews
from .views import authviews
from .views import userstatviews

urlpatterns = [
    # Tournament and games related end points including scoreboard
    path("tournaments/", tournamentviews.TournamentList.as_view()),
    path("tournaments/<int:pk>/games/", tournamentviews.TournamentGameList.as_view()),
    path(
        "tournaments/<int:pk>/scoreboard/",
        tournamentviews.TournamentScoreborad.as_view(),
    ),
    # Team related (team -> players) end points
    path("teams/", teamviews.TeamList.as_view()),
    path("teams/<int:pk>/", teamviews.TeamDetail.as_view()),
    path("teams/<int:pk>/players/", teamviews.PlayerListForTeam.as_view()),
    path(
        "teams/<int:pk>/avgpercentileplayers/",
        teamviews.PlayerListWithAveragePercentile.as_view(),
    ),
    # Player related endpoints
    path("players/<int:pk>/", playerviews.PlayerDetail.as_view()),
    # Coach related end points
    path("coaches/", coachviews.CoachList.as_view()),
    # Get auth token
    # path("authorize/", views.obtain_auth_token),
    path("authorize/", authviews.CustomAuthToken.as_view()),
    path("logout/", authviews.Logout.as_view()),
    # User stat related end points
    path("userstats/", userstatviews.Userstat.as_view()),
    path("onlineusers/", userstatviews.OnlineUsers.as_view()),
]
