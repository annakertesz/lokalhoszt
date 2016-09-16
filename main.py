import pygame
from character import Character
from lifebar import Lifebar

pygame.init()


#main settings
display = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('localhost')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

background_image = pygame.image.load("images/background.jpg").convert()
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

#MAIN LOOP
game_over = False
while not game_over:
    game_over = char_1.life <= 0 or char_2.life <= 0
    char_1_life = Lifebar(display, char_1, 20, 20)
    char_2_life = Lifebar(display, char_2, 700, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
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

    for character in characters:
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
    char_1_life.show()
    char_2_life.show()
    char_1.show_img()
    char_2.show_img()
    pygame.display.update()

    clock.tick(60)


pygame.quit()
