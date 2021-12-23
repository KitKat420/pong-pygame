import pygame
from pygame.constants import K_s, K_w
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle

STEP = 5
FPS = 60
WIDTH, HEIGHT = 750, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
PADDLE_WIDTH, PADDLE_HEIGHT = 25, 100
pygame.display.set_caption("Pong")


scoreboard = Scoreboard()
clock = pygame.time.Clock()
l_paddle = Paddle(50, 250)
r_paddle = Paddle(675, 250)
ball = Ball()


def draw_window():
    """draws rectangles and updates display"""
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, l_paddle)
    pygame.draw.rect(WINDOW, WHITE, r_paddle)
    pygame.draw.rect(WINDOW, WHITE, ball)
    render_score = scoreboard.score_text()

    pygame.Surface.blit(WINDOW, render_score,
                        (WIDTH / 2 - render_score.get_width() / 2, 25))
    ball.reset_ball()
    pygame.display.update()


def main():
    is_game_on = True
    while is_game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_on = False

        l_paddle.controls(pygame.key.get_pressed())
        r_paddle.paddle_automation()
        ball.ball_automation()
        ball.bounce(l_paddle)
        ball.bounce(r_paddle)

        if ball.x == 0:
            scoreboard.computer_score += 1
        elif ball.x == WIDTH - 5:
            scoreboard.player_score += 1

        draw_window()

    pygame.display.quit()


main()
