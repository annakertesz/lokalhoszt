import pygame
from character import Character
from lifebar import Lifebar
from sounds import *
import random
from bloodpattern import BloodPattern

pygame.init()


#main settings
display = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('localhost')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

background_image = pygame.image.load("images/background.jpg").convert()
picture1 = pygame.image.load('images/1-blood-png-image.png').convert_alpha()
picture2 = pygame.image.load('images/2-blood-png-image.png').convert_alpha()
picture3 = pygame.image.load('images/4-blood-png-image.png').convert_alpha()
movestages = {
                       'stand': pygame.image.load('images/stand.png').convert_alpha(),
                       'crouch': pygame.image.load('images/crouch.png').convert_alpha(),
                       'jump': pygame.image.load('images/jump.png').convert_alpha(),
                       'kick': pygame.image.load('images/kick.png').convert_alpha(),
                       'punch': pygame.image.load('images/punch.png').convert_alpha(),
                       'block': pygame.image.load('images/block.png').convert_alpha(),
                       'head': pygame.image.load('images/head.png').convert_alpha()
             }


char_1 = Character(20, 20, "right", movestages, display)
char_2 = Character(100, 100, "right", movestages, display)
char_1.opponent = char_2
char_2.opponent = char_1
characters = [char_1, char_2]

characters = [char_1, char_2]

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

on = True
# display.blit(story_1, [0, 0])
# clock.tick(200)
# display.blit(story_2, [0, 0])
# clock.tick(200)
# display.blit(story_3, [0, 0])
# clock.tick(200)
while on:
    game_over = False
    char_1.life = 100
    char_2.life = 100
    while not game_over:
        game_over = char_1.life <= 0 or char_2.life <= 0
        if game_over:
            if char_1.life < 1:
                char_2.won += 1
            if char_2.life < 1:
                char_1.won += 1
            if char_1.won == 3 or char_2.won == 3:
                on = False
        char_1_life = Lifebar(display, char_1, 20, 20)
        char_2_life = Lifebar(display, char_2, 700, 20)
        before_l1 = char_1.life
        before_l2 = char_2.life
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                on = False

            if event.type == JOYAXISMOTION:
                if (e.dict['axis'] == 0):
                    axis = "X"
                    print(1)

                if (e.dict['axis'] == 1):
                    axis = "Y"
                    print(1)
                else:
                    print(1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    char_1.moves.append("right")
                if event.key == pygame.K_LEFT:
                    char_1.moves.append("left")
                if event.key == pygame.K_d:
                    char_2.moves.append("right")
                if event.key == pygame.K_a:
                    char_2.moves.append("left")
                if event.key == pygame.K_w:
                    if char_2.in_jump <= 0:
                        char_2.in_jump = 50
                if event.key == pygame.K_UP:
                    if char_1.in_jump <= 0:
                        char_1.in_jump = 50
                if event.key == pygame.K_s:
                    char_2.crouch_stage = True
                if event.key == pygame.K_DOWN:
                    char_1.crouch_stage = True
            # PUNCH
                elif event.key == pygame.K_l:
                    char_1.punch()
                elif event.key == pygame.K_SPACE:
                    char_2.punch()

            # HEAD
                elif event.key == pygame.K_k:
                    char_1.head()
                elif event.key == pygame.K_x:
                    char_2.head()
            # KICK
                elif event.key == pygame.K_j:
                    char_1.kick()
                elif event.key == pygame.K_c:
                    char_2.kick()

                if event.key == pygame.K_m:
                    char_1.block()
                if event.key == pygame.K_n:
                    char_2.block()
                if event.key == pygame.K_y:
                    random.choice(characters).life = 100
            # -------------------------
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    char_1.moves.remove("right")

                if event.key == pygame.K_LEFT:
                    char_1.moves.remove("left")
                if event.key == pygame.K_d:
                    char_2.moves.remove("right")
                if event.key == pygame.K_a:
                    char_2.moves.remove("left")
                if event.key == pygame.K_s:
                    char_2.crouch_stage = False
                if event.key == pygame.K_DOWN:
                    char_1.crouch_stage = False
                if event.key == pygame.K_m:
                    char_1.block_out()
                if event.key == pygame.K_n:
                    char_2.block_out()

        for character in characters:
            if character.stage == 'block':
                if character.blockpower > 200:
                    character.blockpower -= 200
                else:
                    character.block_out()
            if character.blockpower < 10000:
                character.blockpower += 50
            character.jump_step()
            character.crouch()
            for direction in character.moves:
                character.move(direction)
            character.in_punch -= 1
            character.in_head -= 1
            character.in_kick -= 1
            if character.in_punch <= 0 and character.stage == 'punch':
                character.stage = 'stand'
            if character.crouch_stage is False and character.stage == 'crouch':
                character.stage = 'stand'
            if character.in_jump <= 0 and character.stage == 'jump':
                character.stage = 'stand'
            if character.in_head <= 0 and character.stage == 'head':
                character.stage = 'stand'
            if character.in_kick <= 0 and character.stage == 'kick':
                character.stage = 'stand'

        display.blit(background_image, [0, 0])
        after_l1 = char_1.life
        after_l2 = char_2.life
        char_1.show_img()
        char_2.show_img()
        brutality_level = before_l2 + before_l1 - after_l2 - after_l1
        if brutality_level > 1:
            BloodPattern.add_pattern(int(brutality_level/10), random.choice([picture1]))
        for pattern in BloodPattern.bps:
            pattern.duration -= 1
            if pattern.duration > 0:
                for p in pattern.patterns:
                    display.blit(p[0], p[1])
        char_1_life.show()
        char_2_life.show()
        pygame.display.update()

        clock.tick(60)

pygame.quit()
