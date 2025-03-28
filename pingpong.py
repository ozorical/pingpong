import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_speed_x, ball_speed_y = 5, 5
left_paddle_speed, right_paddle_speed = 0, 0
left_score, right_score = 0, 0
font = pygame.font.Font(None, 74)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle_speed = -8
            elif event.key == pygame.K_s:
                left_paddle_speed = 8
            elif event.key == pygame.K_UP:
                right_paddle_speed = -8
            elif event.key == pygame.K_DOWN:
                right_paddle_speed = 8
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                left_paddle_speed = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                right_paddle_speed = 0

    left_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, left_paddle.y + left_paddle_speed))
    right_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, right_paddle.y + right_paddle_speed))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1.1

    if ball.left <= 0:
        right_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -5
    elif ball.right >= WIDTH:
        left_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = 5

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle, border_radius=10)
    pygame.draw.rect(screen, WHITE, right_paddle, border_radius=10)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    screen.blit(font.render(str(left_score), True, WHITE), (WIDTH // 4, 20))
    screen.blit(font.render(str(right_score), True, WHITE), (WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(60)
