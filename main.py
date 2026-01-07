import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
# Set the caption of the window
pygame.display.set_caption("Runner")

# 2.1 initialize the clock to set the frame rate
clock = pygame.time.Clock()

test_font = pygame.font.Font("./font/Pixeltype.ttf", 60)

# 2.3 create a surface
sky_surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()

score_surface = test_font.render("My Game", False, 'Black')  
score_rect = score_surface.get_rect(center  = (400, 50)) 

snail_surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha() 
snail_rect = snail_surface.get_rect(bottomright = (800, 300)) 

player_surface = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        # Check if the event is a quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Over")
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 10)
    screen.blit(score_surface, score_rect)

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect) 

    # if player_rect.colliderect(snail_rect):
    #     print("Collision")

    pygame.display.update()
    clock.tick(60) 