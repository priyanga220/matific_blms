from core.models import Game, GameStat, Tournament
from core.enums import GameStatus


class GameService:

    def loadTournaments(self) -> list[Tournament]:
        return Tournament.objects.all().order_by("-created_date")

    def loadTournamentGames(self, tournament_id: int) -> list[Game]:
        return Game.objects.filter(tournament_id=tournament_id).order_by("-date")

    def loadScoreboard(self, tournament_id: int):

        games: list[Game] = Game.objects.filter(tournament_id=tournament_id).exclude(
            game_status=GameStatus.SC
        )
        scoreboard: list = []
        number: int = len(games)
        for game in games:
            entry = {}
            entry["game"] = {
                "game_no": number,
                "game_level": game.game_level.name,
                "game_status": game.game_status.name,
                "game_date_time": game.date,
            }
            number = number - 1
            gamestats: list[GameStat] = game.gamestats.all()

            gamestats1: GameStat = gamestats[0]
            entry["team1"] = (
                f"{gamestats1.team.name} - [{gamestats1.team.displayname}]"
                if gamestats1.team
                else gamestats1.teamref
            )
            entry["team1_score"] = gamestats1.score | 0
            entry["team1_winner"] = "Y" if gamestats1.iswinner else "N"

            gamestats2: GameStat = gamestats[1]
            entry["team2"] = (
                f"{gamestats2.team.name} - [{gamestats2.team.displayname}]"
                if gamestats2.team
                else gamestats1.teamref
            )
            entry["team2_score"] = gamestats2.score | 0
            entry["team2_winner"] = "Y" if gamestats2.iswinner else "N"

            scoreboard.append(entry)
            print(scoreboard)
        return scoreboard
