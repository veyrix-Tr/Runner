import random
import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, jump_sound):
        super().__init__()

        self.jump_sound = jump_sound
        self.player_jump = pygame.image.load("./graphics/Player/jump.png").convert_alpha() 
        self.player_walk = [pygame.image.load("./graphics/Player/player_walk_1.png").convert_alpha(), pygame.image.load("./graphics/Player/player_walk_2.png").convert_alpha()]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]

        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()  
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and self.rect.bottom >= 300:
                self.gravity = -20
                self.jump_sound.play()  
             
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state() 
 

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type):
        super().__init__()
        self.obstacle_type = obstacle_type
        if obstacle_type == "snail":
            snail_1 = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("./graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        elif obstacle_type == "fly":
            fly_1 = pygame.image.load("./graphics/Fly/Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("./graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 190

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1200), y_pos))
 
    def animation_state(self):
        self.index += 0.1
        if self.index >= len(self.frames): self.index = 0
        self.image = self.frames[int(self.index)]

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

def display_score():
    score = int((pygame.time.get_ticks()-start_time) / 700) 
    score_surface = test_font.render(f"Score:  {score}", False, (64,64,64 ))  
    score_rect = score_surface.get_rect(center  = (400, 50))

    # for background color ehind the score
    bg_rect = score_rect.inflate(1, 1)
    pygame.draw.rect(screen, '#c0e8ec', bg_rect)
    pygame.draw.rect(screen, '#c0e8ec', bg_rect, 3)

    screen.blit(score_surface, score_rect)
    return score


def collision(player, obstacles):
    if pygame.sprite.spritecollide(player, obstacles, False):
        obstacles.empty()
        return False
    return True  

pygame.init()

screen = pygame.display.set_mode((800, 400))
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

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player(jump_sound))
obstacles = pygame.sprite.Group()

# Surfaces
sky_surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()


# Intro Surfaces
player_stand = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom (player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200)) 

game_name = test_font.render("Pixel-Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press Space to run", False, (111, 216, 169))
game_message_rect = game_message.get_rect(center = (400, 340))

score_message = test_font.render(f"Your score: {score}", False, (111, 216, 169))
score_message_rect = score_message.get_rect(center = (400, 340))


# Timer for obstacles
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        # Check if the event is a quit event
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            print("Game Over")
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                if bg_music.get_volume() == 0:
                    bg_music.set_volume(0.2)
                else:
                    bg_music.set_volume(0)
            if event.type == obstacle_timer:
                obstacles.add(Obstacle(random.choice(["snail", "fly", "snail"])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and (pygame.time.get_ticks()- score*700 - start_time) > 700:
                game_active = True
                bg_music.play(loops=-1)
                player.sprite.rect.midbottom = (80, 300)
                player.sprite.gravity = 0
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        
        score =  display_score()

        player.draw(screen)
        player.update()
        obstacles.draw(screen)
        obstacles.update() 
        
        game_active = collision(player.sprite, obstacles)

    else:
        bg_music.stop()
        screen.fill((94,129,162)) 
        screen.blit(player_stand, player_stand_rect) 
        screen.blit(game_name, game_name_rect)
        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)