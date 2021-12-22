import pygame
from pygame.constants import K_s, K_w
from ball import Ball
from scoreboard import Scoreboard

pygame.init()

STEP = 5
FPS = 60
WIDTH, HEIGHT = 750, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
PADDLE_WIDTH, PADDLE_HEIGHT = 25, 100
pygame.display.set_caption("Pong")

# global variables for ball automation
step_x = 5
step_y = 5

scoreboard = Scoreboard()
clock = pygame.time.Clock()

font = pygame.font.Font("./Assets/PressStart2P-Regular.ttf", 15)


def score_text(player_score, computer_score):
    return pygame.font.Font.render(
        font, f"SCORE: {player_score} | {computer_score}", False, WHITE, None)


l_paddle = pygame.Rect(50, 250 - PADDLE_HEIGHT / 2,
                       PADDLE_WIDTH, PADDLE_HEIGHT)
r_paddle = pygame.Rect(675, 250 - PADDLE_HEIGHT / 2,
                       PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, 20, 20)


def draw_window():
    """draws rectangles and updates display"""
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, l_paddle)
    pygame.draw.rect(WINDOW, WHITE, r_paddle)
    pygame.draw.rect(WINDOW, WHITE, ball)
    render_score = score_text(
        scoreboard.player_score, scoreboard.computer_score)

    pygame.Surface.blit(WINDOW, render_score,
                        (WIDTH / 2 - render_score.get_width() / 2, 25))
    reset_ball(ball)
    pygame.display.update()


def l_paddle_controls(key_pressed, paddle):
    """left paddle controls"""
    if key_pressed[K_w]:
        paddle.y -= STEP

    if key_pressed[K_s]:
        paddle.y += STEP


direction = 5


def paddle_automation(paddle):
    """Handles computer paddle movement"""
    global direction
    paddle.y += direction

    if paddle.y == HEIGHT - 125:
        direction *= -1

    elif paddle.y == 25:
        direction *= -1


def reset_ball(ball):
    """Resets the position of ball"""
    if ball.x < 0 or ball.x > WIDTH:
        ball.left = WIDTH / 2
        ball.top = HEIGHT / 2
    else:
        pass


def bounce(ball, paddle):
    """detects collision of ball and paddle"""
    collided = pygame.Rect.collidepoint(paddle, ball.x, ball.y)
    global step_x
    if collided:
        step_x *= -1


def ball_automation(ball):
    """Moves ball and changes direction of ball"""
    global step_x
    global step_y
    ball.x += step_x
    ball.y -= step_y

    if ball.y == 0 or ball.y == HEIGHT - ball.height:
        step_y *= -1


def current_score(ball):
    """Keeps track of computer and player score"""
    if ball.x == 0:
        scoreboard.increase_computer_score()
        print(f"computer score: {scoreboard.computer_score}")
    elif ball.x == WIDTH - 5:
        scoreboard.increase_player_score()
        print(f"player score: {scoreboard.player_score}")


def main():
    is_game_on = True
    while is_game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_on = False

        key_pressed = pygame.key.get_pressed()

        l_paddle_controls(key_pressed, l_paddle)
        paddle_automation(r_paddle)
        ball_automation(ball)
        bounce(ball, l_paddle)
        bounce(ball, r_paddle)
        current_score(ball)
        draw_window()

    pygame.display.quit()


main()
