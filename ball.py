from pygame import Rect
import pygame

WIDTH, HEIGHT = 750, 500


class Ball(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT / 2, 20, 20)
        self.step_x = 5
        self.step_y = 5

    def reset_ball(self):
        """Resets the position of ball"""
        if self.x < 0 or self.x > WIDTH:
            self.left = WIDTH / 2
            self.top = HEIGHT / 2

    def ball_automation(self):
        """Moves ball and changes direction of ball"""
        self.x += self.step_x
        self.y -= self.step_y

        if self.y == 0 or self.y == HEIGHT - self.height:
            self.step_y *= -1

    def bounce(self, paddle):
        """detects collision of ball and paddle"""

        "will fix later when solution is found"
        collided = pygame.Rect.collidepoint(paddle, self.x, self.y)
        if collided:
            self.step_x *= -1
