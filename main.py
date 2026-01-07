import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
# Set the caption of the window
pygame.display.set_caption("Runner")

# 2.1 initialize the clock to set the frame rate
clock = pygame.time.Clock()

# 2.3 create a surface
test_surface = pygame.image.load("./graphics/Sky.png")

while True:
    for event in pygame.event.get():
        # Check if the event is a quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Over")
            exit()

    screen.blit(test_surface, (0, 0))
    pygame.display.update()
    clock.tick(60) 