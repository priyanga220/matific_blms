from enum import Enum

class GameStatus(Enum):
    SC = "Scheduled"
    PL = "Playing"
    AB = "Abandoned"
    CR = "Completed with Result"
    CT = "Completed with Tie"