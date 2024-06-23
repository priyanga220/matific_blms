from django.urls import path
from rest_framework.authtoken import views

from .views import teamviews
from .views import playerviews
from .views import tournamentviews
from .views import coachviews
from .views import authviews
from .views import userstatviews

app_name = "restapi"
urlpatterns = [
    # Get auth token
    path(
        "authentication/", authviews.Authentication.as_view(), name="authenticate-user"
    ),
    # Logout
    path("logout/", authviews.Logout.as_view(), name="logout-user"),
    # Tournament and games related end points including scoreboard
    path(
        "tournaments/", tournamentviews.TournamentList.as_view(), name="tournament-list"
    ),
    path(
        "tournaments/<int:pk>/games/",
        tournamentviews.TournamentGameList.as_view(),
        name="game-list-for-tournament",
    ),
    path(
        "tournaments/<int:pk>/scoreboard/",
        tournamentviews.TournamentScoreborad.as_view(),
        name="scoreboard-for-tournament",
    ),
    # Team related (team -> players) end points
    path("teams/", teamviews.TeamList.as_view(), name="team-list"),
    path("teams/<int:pk>/", teamviews.TeamDetail.as_view(), name="team-detail"),
    path(
        "teams/<int:pk>/players/",
        teamviews.PlayerListForTeam.as_view(),
        name="player-list-for-team",
    ),
    path(
        "teams/<int:pk>/avgpercentileplayers/",
        teamviews.PlayerListWithAveragePercentile.as_view(),
        name="player-list-aboveavg-percentile-for-team",
    ),
    # Player related endpoints
    path("players/<int:pk>/", playerviews.PlayerDetail.as_view(), name="player-detail"),
    # Coach related end points
    path("coaches/", coachviews.CoachList.as_view(), name="coach-list"),
    # User stat related end points
    path("userstats/", userstatviews.Userstat.as_view(), name="userstat-list"),
    path("onlineusers/", userstatviews.OnlineUsers.as_view(), name="online-user-list"),
]
