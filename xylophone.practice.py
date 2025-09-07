import pygame
import sys

pygame.init()

# Screen setup
width, height = 1000, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Xylophone")

FPS = 20
clock = pygame.time.Clock()

# Colors
RED = (76, 0, 0)
ORANGE = (255, 185, 0)
YELLOW = (90, 255, 0)
GREEN = (0, 56, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)
WHITE = (255, 255, 255)

# Load sounds
sound1 = pygame.mixer.Sound("note1.mp3")
sound2 = pygame.mixer.Sound("note2.mp3")
sound3 = pygame.mixer.Sound("note3.mp3")
sound4 = pygame.mixer.Sound("noteA.mp3")
sound5 = pygame.mixer.Sound("noteB.mp3")
sound6 = pygame.mixer.Sound("noteC.mp3")
sound7 = pygame.mixer.Sound("noteD.mp3")
sound8 = pygame.mixer.Sound("noteE.mp3")

# Small rect (player)
small_rect_x = 100
small_rect_y = 100
small_rect_speed = 20
small_rect_size = 40

# Game loop
running = True
while running:
    screen.fill("blue")

    # Draw keys (x position spaced by 80)
    key1 = pygame.draw.rect(screen, RED, (0,   100, 70, 250))
    key2 = pygame.draw.rect(screen, ORANGE, (80, 100, 70, 250))
    key3 = pygame.draw.rect(screen, YELLOW, (160, 100, 70, 250))
    key4 = pygame.draw.rect(screen, GREEN, (240, 100, 70, 250))
    key5 = pygame.draw.rect(screen, BLUE, (320, 100, 70, 250))
    key6 = pygame.draw.rect(screen, INDIGO, (400, 100, 70, 250))
    key7 = pygame.draw.rect(screen, VIOLET, (480, 100, 70, 250))
    key8 = pygame.draw.rect(screen, RED, (560, 100, 70, 250))

    # Draw player rect
    small_rect = pygame.draw.rect(
        screen, WHITE, (small_rect_x, small_rect_y, small_rect_size, small_rect_size)
    )

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                small_rect_x -= small_rect_speed
            if event.key == pygame.K_RIGHT:
                small_rect_x += small_rect_speed
            if event.key == pygame.K_UP:
                small_rect_y -= small_rect_speed
            if event.key == pygame.K_DOWN:
                small_rect_y += small_rect_speed

    # Collision check with sounds
    if small_rect.colliderect(key1):
        sound1.play()
    if small_rect.colliderect(key2):
        sound2.play()
    if small_rect.colliderect(key3):
        sound3.play()
    if small_rect.colliderect(key4):
        sound4.play()
    if small_rect.colliderect(key5):
        sound5.play()
    if small_rect.colliderect(key6):
        sound6.play()
    if small_rect.colliderect(key7):
        sound7.play()
    if small_rect.colliderect(key8):
        sound8.play()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit() 


