import pygame
from pygame.constants import K_s, K_w

STEP = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 25, 100
WIDTH, HEIGHT = 750, 500


class Paddle(pygame.Rect):
    def __init__(self, x_position, y_position):
        self.direction = 5
        self.x_coord = x_position
        self.y_coord = y_position
        super().__init__(self.x_coord, self.y_coord - PADDLE_HEIGHT / 2,
                         PADDLE_WIDTH, PADDLE_HEIGHT)

    def controls(self, key_pressed):
        """left paddle controls"""
        if key_pressed[K_w]:
            print("moved up")
            self.y -= STEP

        if key_pressed[K_s]:
            print("moved down")
            self.y += STEP

    def paddle_automation(self):
        """Handles computer paddle movement"""
        self.y += self.direction

        if self.y == HEIGHT - 125:
            self.direction *= -1
        elif self.y == 25:
            self.direction *= -1
