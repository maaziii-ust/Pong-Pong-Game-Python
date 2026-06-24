import pygame
import sys

pygame.init()

# ---------- WINDOW ----------
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Pong Game")

clock = pygame.time.Clock()
FPS = 60

# ---------- COLORS ----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ---------- PADDLES ----------
paddle_width = 15
paddle_height = 100
paddle_speed = 7

left_paddle = pygame.Rect(30, screen_height//2 - paddle_height//2, paddle_width, paddle_height)
right_paddle = pygame.Rect(screen_width - 45, screen_height//2 - paddle_height//2, paddle_width, paddle_height)

# ---------- BALL ----------
ball_size = 15
ball = pygame.Rect(screen_width//2 - 7, screen_height//2 - 7, ball_size, ball_size)
ball_dx = 5
ball_dy = 5

# ---------- SCORE ----------
left_score = 0
right_score = 0
font = pygame.font.SysFont(None, 50)

# ---------- DRAW ----------
def draw_window():
    gameWindow.fill(BLACK)

    pygame.draw.rect(gameWindow, WHITE, left_paddle)
    pygame.draw.rect(gameWindow, WHITE, right_paddle)
    pygame.draw.ellipse(gameWindow, WHITE, ball)

    pygame.draw.line(gameWindow, WHITE, (screen_width//2, 0), (screen_width//2, screen_height), 2)

    #Show Scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    gameWindow.blit(left_text, (screen_width//4, 20))
    gameWindow.blit(right_text, (screen_width*3//4, 20))

    pygame.display.update()

# ---------- MAIN LOOP ----------
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Left paddle
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < screen_height:
        left_paddle.y += paddle_speed

    # Right paddle
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < screen_height:
        right_paddle.y += paddle_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Wall collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_dy *= -1

    # Paddle collision
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx *= -1

    # Score
    if ball.left <= 0:
        right_score += 1
        ball.center = (screen_width//2, screen_height//2)
        ball_dx *= -1

    if ball.right >= screen_width:
        left_score += 1
        ball.center = (screen_width//2, screen_height//2)
        ball_dx *= -1

    draw_window()
