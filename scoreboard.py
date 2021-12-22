class Scoreboard():
    def __init__(self) -> None:
        self.player_score = 0
        self.computer_score = 0

    def increase_player_score(self):
        self.player_score += 1

    def increase_computer_score(self):
        self.computer_score += 1
