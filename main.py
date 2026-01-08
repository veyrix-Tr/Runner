import random
import pygame
from sys import exit

def display_score():
    score = int((pygame.time.get_ticks()-start_time) / 700) 
    score_surface = test_font.render(f"Score:  {score}", False, (64,64,64 ))  
    score_rect = score_surface.get_rect(center  = (400, 50))

    bg_rect = score_rect.inflate(1, 1)
    pygame.draw.rect(screen, '#c0e8ec', bg_rect)
    pygame.draw.rect(screen, '#c0e8ec', bg_rect, 3)

    screen.blit(score_surface, score_rect)
    return score

def obstacle_movement(obstacle_list):
    if obstacle_list:
        # obstacle_list[:] creates a copy of the list, which is crucial when removing items during iteration
        for obstacle_rect in obstacle_list[:]:
            obstacle_rect.x -= 6

            if obstacle_rect.bottom == 300:  screen.blit(snail_surface, obstacle_rect)
            else: screen.blit(fly_surface, obstacle_rect)

            if obstacle_rect.right < -100:
                obstacle_list.remove(obstacle_rect)
        return obstacle_list
    else: return []

def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True 

def player_animation():
    global player_surface, player_index
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]
    return player_surface

pygame.init()

screen = pygame.display.set_mode((800, 400))
# Set the caption of the window
pygame.display.set_caption("Pixel-Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("./font/Pixeltype.ttf", 60)
game_active = False
start_time = 0
score = 0
jump_sound = pygame.mixer.Sound("./audio/jump.mp3")
jump_sound.set_volume(0.2)
bg_music = pygame.mixer.Sound("./audio/music.wav")
bg_music.set_volume(0.2)

sky_surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()

title_surface = test_font.render("My Game", False, (64,64,64))  
title_rect = title_surface.get_rect(center  = (400, 50)) 

obstacle_rect_list = []

snail_frame1 = pygame.image.load("./graphics/snail/snail1.png").convert_alpha() 
snail_frame2 = pygame.image.load("./graphics/snail/snail2.png").convert_alpha() 
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load("./graphics/Fly/Fly1.png").convert_alpha() 
fly_frame2 = pygame.image.load("./graphics/Fly/Fly2.png").convert_alpha() 
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

player_walk_1 = pygame.image.load("./graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("./graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surface = player_walk[player_index]
player_jump = pygame.image.load("./graphics/Player/jump.png").convert_alpha()

player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0 

player_stand = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom (player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200)) 

game_name = test_font.render("Pixel-Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press Space to run", False, (111, 216, 169))
game_message_rect = game_message.get_rect(center = (400, 340))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 300)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 100)

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
                    jump_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                    jump_sound.play()

                if event.key == pygame.K_m:
                    if bg_music.get_volume() == 0:
                        bg_music.set_volume(0.2)
                    else:
                        bg_music.set_volume(0)

            if event.type == obstacle_timer:
                if random.randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (random.randint(900,1200), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (random.randint(900,1200), 190)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (pygame.time.get_ticks()- score*700 - start_time) > 700:
                game_active = True
                bg_music.play(loops=-1)
                obstacle_rect_list.clear()
                player_rect.midbottom = (80, 300)
                player_gravity = 0
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        
        score =  display_score()

        # snail_rect.x -= 8
        # if snail_rect.right < 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        # floor
        if player_rect.bottom >= 300:player_rect.bottom = 300
        screen.blit(player_animation(), player_rect) 
        
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # if player_rect.colliderect(snail_rect):
        #     game_active = False
        game_active = collision(player_rect, obstacle_rect_list)

    else:
        bg_music.stop()
        screen.fill((94,129,162)) 
        screen.blit(player_stand, player_stand_rect) 

        score_message = test_font.render(f"Your score: {score}", False, (111, 216, 169))
        score_message_rect = score_message.get_rect(center = (400, 340))

        screen.blit(game_name, game_name_rect)
        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)