import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
BALL_COLOR = (255, 50, 50)
PADDLE_COLOR = (255, 255, 255)
BG_COLOR = (10, 10, 30)  # Dark theme background

# Score
score = 0
font = pygame.font.Font(None, 36)

# Paddle
paddle_width, paddle_height = 100, 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 50, paddle_width, paddle_height)

# Ball
ball_size = 10
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_size, ball_size)
ball_dx, ball_dy = 3, -3  # Initial speed

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = WIDTH // brick_cols - 5
brick_height = 20
bricks = []

colors = [(255, 0, 0), (255, 100, 0), (255, 200, 0), (100, 255, 0), (0, 255, 100)]  # Gradient Colors

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * (brick_width + 5), row * (brick_height + 5) + 50, brick_width, brick_height)
        bricks.append((brick, colors[row]))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BG_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-7, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(7, 0)

    # Ball movement
    ball.move_ip(ball_dx, ball_dy)

    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # Ball collision with bricks
    for brick, color in bricks[:]:
        if ball.colliderect(brick):
            ball_dy = -ball_dy
            bricks.remove((brick, color))
            score += 1
            ball_dx *= 1.05  # Increase speed when score increases
            ball_dy *= 1.05

    # Ball falls below screen
    if ball.bottom >= HEIGHT:
        running = False

    # Draw paddle
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, BALL_COLOR, ball)

    # Draw bricks
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()