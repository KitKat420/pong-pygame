import pygame

pygame.init()

WHITE = (255, 255, 255)
FONT = pygame.font.Font("./Assets/PressStart2P-Regular.ttf", 15)


class Scoreboard():
    def __init__(self) -> None:
        self.player_score = 0
        self.computer_score = 0

    def score_text(self):
        return pygame.font.Font.render(
            FONT, f"SCORE: {self.player_score} | {self.computer_score}", False, WHITE, None)
