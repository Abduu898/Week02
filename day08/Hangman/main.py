import pygame
import os

pygame.init()

base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "assets", "bg.jpg")

screen = pygame.display.set_mode((600, 600))

background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (600, 600))

def draw_stickman(screen):
    white = (255, 255, 255)
    pygame.draw.circle(screen, white, (300, 180), 40, 7)
    pygame.draw.line(screen, white, (300, 220), (300, 360), 7)
    pygame.draw.line(screen, white, (300, 250), (240, 300), 7)
    pygame.draw.line(screen, white, (300, 250), (360, 300), 7)
    pygame.draw.line(screen, white, (300, 360), (250, 450), 7)
    pygame.draw.line(screen, white, (300, 360), (350, 450), 7)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    screen.blit(background, (0, 0))
    draw_stickman(screen)
    pygame.display.update()

pygame.quit()