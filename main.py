import pygame
from sys import exit

pygame.init()

def display_score():
    score = int((pygame.time.get_ticks()-start_time) / 500) 
    score_surface = test_font.render(f"Score:  {score}", False, (64,64,64 ))  
    score_rect = score_surface.get_rect(center  = (400, 50)) 
    screen.blit(score_surface, score_rect)
    return score

screen = pygame.display.set_mode((800, 400))
# Set the caption of the window
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("./font/Pixeltype.ttf", 60)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()

score_surface = test_font.render("My Game", False, (64,64,64 ))  
score_rect = score_surface.get_rect(center  = (400, 50)) 

snail_surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha() 
snail_rect = snail_surface.get_rect(bottomright = (800, 300)) 

player_surface = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0 

player_stand = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom (player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200)) 

game_name = test_font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press Space to run", False, (111, 216, 169))
game_message_rect = game_message.get_rect(center = (400, 340))

while True:
    for event in pygame.event.get():
        # Check if the event is a quit event
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            print("Game Over")
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20 
                    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (pygame.time.get_ticks()- score*500 - start_time) > 500:
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        score =  display_score()

        snail_rect.x -= 8
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect) 

        if player_rect.colliderect(snail_rect):
            game_active = False

    else:
        screen.fill((94,129,162)) 
        screen.blit(player_stand, player_stand_rect) 

        score_message = test_font.render(f"Your score: {score}", False, (111, 216, 169))
        score_message_rect = score_message.get_rect(center = (400, 340))

        screen.blit(game_name, game_name_rect)
        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)