from pygame import Rect
import pygame


class Ball(Rect):

    def __init__(self, screen_width, screen_height):
        self.WIDTH = screen_width
        self.HEIGHT = screen_height
        super().__init__()
        self.top = self.HEIGHT / 2
        self.left = self.WIDTH / 2
        self.height = 20
        self.width = 20
        self.step_x = 5
        self.step_y = 5

    def bounce_y(self):
        self.step_y *= -1

    def bounce_x(self):
        self.step_x *= -1
