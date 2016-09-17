import pygame
from character import *
from lifebar import Lifebar
from pygame.locals import *
from sounds import *
import random

pygame.init()


#main settings

display = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
print(infoObject.current_w, infoObject.current_h)
pygame.display.set_caption('localhost')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

background_image = pygame.image.load("images/background.png").convert()

movestages = {
                       'stand': pygame.image.load('images/stand.png').convert_alpha(),
                       'crouch': pygame.image.load('images/crouch.png').convert_alpha(),
                       'jump': pygame.image.load('images/jump.png').convert_alpha(),
                       'kick': pygame.image.load('images/kick.png').convert_alpha(),
                       'punch': pygame.image.load('images/punch.png').convert_alpha(),
                       'block': pygame.image.load('images/block.png').convert_alpha(),
                       'head': pygame.image.load('images/head.png').convert_alpha()
             }


char_1 = Character(0 , infoObject.current_h - 600, "right", movestages, display)
char_2 = Character(infoObject.current_w - 250, infoObject.current_h - 600, "left", movestages, display)
char_1.opponent = char_2
char_2.opponent = char_1
characters = [char_1, char_2]
# JOYSTICK
try:
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joysticks[0].init()
    joysticks[1].init()
    player1_joystick = joysticks[0]
    player2_joystick = joysticks[1]
except IndexError:
    player1_joystick = None
    player2_joystick = None

mixer.music.set_volume(0.4)
# mixer.music.play(-1)


on = True
# display.blit(story_1, [0, 0])
# clock.tick(1000)
# display.blit(story_2, [0, 0])
# clock.tick(1000)
# display.blit(story_3, [0, 0])
# clock.tick(1000)
while on:

    game_over = False
    char_1.life = 100
    char_2.life = 100
    while not game_over:
        char_1.checking_overlaping()
        char_2.checking_overlaping()
        char_1.space_limit()
        char_2.space_limit()
        game_over = char_1.life <= 0 or char_2.life <= 0
        if game_over:
            if char_1.life < 1:
                char_2.won += 1
            if char_2.life < 1:
                char_1.won += 1
            if char_1.won == 3 or char_2.won == 3:
                on = False
        char_1_life = Lifebar(display, char_1, 20, 20)
        char_2_life = Lifebar(display, char_2, infoObject.current_h + 250, 20)
    # JOYSTICK INPUT

        for event in pygame.event.get():

        # JOYSTICK INPUT
            if event.type == pygame.locals.JOYAXISMOTION:
                player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
                player2jx, player2jy = player2_joystick.get_axis(0), player2_joystick.get_axis(1)
                if player1jx < 0:
                    char_1.moves.append("left")
                elif player1jx > 0:
                    char_1.moves.append("right")
                if player1jy < 0:
                    if char_1.in_jump <= 0:
                        char_1.in_jump = 50
                elif player1jy > 0:
                    char_1.crouch_stage = True
                if player2jx < 0:
                    char_2.moves.append("left")
                elif player2jx > 0:
                    char_2.moves.append("right")
                if player2jy < 0:
                    if char_2.in_jump <= 0:
                        char_2.in_jump = 50
                elif player2jy > 0:
                    char_2.crouch_stage = True
        if player1_joystick.get_button(0):
            char_1.punch()
        elif player2_joystick.get_button(0):
            char_2.punch()
        elif player1_joystick.get_button(1):
            char_1.head()
        elif player2_joystick.get_button(1):
            char_2.head()
        elif player1_joystick.get_button(2):
            char_1.kick()
        elif player2_joystick.get_button(2):
            char_2.kick()
        elif player1_joystick.get_button(3):
            char_1.block()
        elif player2_joystick.get_button(3):
            char_2.block()
        # # KEYBOARD INPUT
        # else:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             game_over = True
        #             on = False
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_RIGHT:
        #                 char_1.moves.append("right")
        #             elif event.key == pygame.K_LEFT:
        #                 char_1.moves.append("left")
        #             elif event.key == pygame.K_d:
        #                 char_2.moves.append("right")
        #             elif event.key == pygame.K_a:
        #                 char_2.moves.append("left")
        #             elif event.key == pygame.K_w:
        #                 if char_2.in_jump <= 0:
        #                     char_2.in_jump = 50
        #             elif event.key == pygame.K_UP:
        #                 if char_1.in_jump <= 0:
        #                     char_1.in_jump = 50
        #             elif event.key == pygame.K_s:
        #                 char_2.crouch_stage = True
        #             elif event.key == pygame.K_DOWN:
        #                 char_1.crouch_stage = True
        #         # PUNCH
        #             elif event.key == pygame.K_l:
        #                 char_1.punch()
        #             elif event.key == pygame.K_SPACE:
        #                 char_2.punch()
        #
        #         # HEAD
        #             elif event.key == pygame.K_k:
        #                 char_1.head()
        #             elif event.key == pygame.K_x:
        #                 char_2.head()
        #         # KICK
        #             elif event.key == pygame.K_j:
        #                 char_1.kick()
        #             elif event.key == pygame.K_c:
        #                 char_2.kick()
        #
        #             elif event.key == pygame.K_m:
        #                 char_1.block()
        #             elif event.key == pygame.K_n:
        #                 char_2.block()
        #             elif event.key == pygame.K_y:
        #                 random.choice(characters).life = 100
        #         # -------------------------
        #         elif event.type == pygame.KEYUP:
        #             if event.key == pygame.K_RIGHT:
        #                 char_1.moves.remove("right")
        #
        #             elif event.key == pygame.K_LEFT:
        #                 char_1.moves.remove("left")
        #             elif event.key == pygame.K_d:
        #                 char_2.moves.remove("right")
        #             elif event.key == pygame.K_a:
        #                 char_2.moves.remove("left")
        #             elif event.key == pygame.K_s:
        #                 char_2.crouch_stage = False
        #             elif event.key == pygame.K_DOWN:
        #                 char_1.crouch_stage = False
        #             elif event.key == pygame.K_m:
        #                 char_1.block_out()
        #             elif event.key == pygame.K_n:
        #                 char_2.block_out()

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

        display.blit(pygame.transform.scale(background_image, (infoObject.current_w, infoObject.current_h)),(0, 0))
        char_1_life.show()
        char_2_life.show()
        char_1.show_img()
        char_2.show_img()
        pygame.display.update()
        clock.tick(60)

pygame.quit()
