from ..serializers.teamserializer import *
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Avg

import numpy as np

from core.models import Team
from core.models import GameStat
from core.models import Player
from core.models import PlayerStat


class TeamService:

    def loadTeams(self) -> list[Team]:
        return Team.objects.all().order_by("name")

    def loadTeamView(self, teamId: int):
        team = self.get_object(teamId)
        avg = GameStat.objects.filter(team_id=teamId).aggregate(Avg("score"))
        result = {
            "teamid": team.id,
            "name": team.name,
            "displayname": team.displayname,
            "rank": team.rank,
            "slogan": team.slogan,
            "average_score": avg.get("score__avg"),
        }
        return result

    def loadPlayerListForTeam(self, teamId: int) -> list[Player]:
        team = self.get_object(teamId)
        return team.players

    # return players for a team which has the average score across the team above or in
    # the given percentile
    def loadPlayerListForTeamAboveGivenPercentileScore(
        self, teamId: int, percent: int
    ) -> list[Player]:

        percent_i = int(percent)
        players = self.loadPlayerListForTeam(teamId).all()
        playerAvgScoreMap = {}
        # calculate the average score of players and keep as a map [playerId : avgScore]
        # defults to zero if no stats
        for player in players:
            playerAvgScoreMap[player.id] = (
                PlayerStat.objects.filter(player_id=player.id).aggregate(Avg("score"))[
                    "score__avg"
                ]
                or 0
            )

        # calculate the percentile score for the given percentile for all average scores of team
        percentile_score: float = np.percentile(
            list(playerAvgScoreMap.values()), percent_i
        )
        # get the players with average score above or equal to the percentile score
        abovepercentile_playerids = list(
            pid for (pid, avg) in playerAvgScoreMap.items() if avg >= percentile_score
        )

        return list(pl for pl in players if pl.id in abovepercentile_playerids)

    def addPlayerToTheTeam(self, team_id: int, player_id: int) -> Player:
        player = get_object_or_404(Player, pk=player_id)
        team = self.get_object(team_id)
        team.players.add(player)
        team.save()
        return player

    def get_object(self, pk: int) -> Team:
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404
