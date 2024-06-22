from django.urls import path

from .views import teamviews
from .views import playerviews
from .views import tournamentviews
from .views import coachviews

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
]
