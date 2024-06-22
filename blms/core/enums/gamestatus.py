from enumchoicefield import ChoiceEnum


class GameStatus(ChoiceEnum):
    SC = "Scheduled"
    PL = "Playing"
    AB = "Abandoned"
    CR = "Completed with Result"
    CT = "Completed with Tie"
