import pygame
from character import Character

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
                       'block': pygame.image.load('images/block.png').convert_alpha()
             }


char_1 = Character(20, 20, "right", movestages, display)
char_2 = Character(100, 100, "right", movestages, display)
char_1.opponent = char_2
char_2.opponent = char_1
characters = [char_1, char_2]

#MAIN LOOP
game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # move
            if event.key == pygame.K_RIGHT:
                char_1.moves.append("right")
            elif event.key == pygame.K_UP:
                char_1.moves.append("up")
            elif event.key == pygame.K_LEFT:
                char_1.moves.append("left")
            elif event.key == pygame.K_DOWN:
                char_1.moves.append("down")
            elif event.key == pygame.K_d:
                char_2.moves.append("right")
            elif event.key == pygame.K_w:
                char_2.moves.append("up")
            elif event.key == pygame.K_a:
                char_2.moves.append("left")
            elif event.key == pygame.K_s:
                char_2.moves.append("down")
            # punch
            elif event.key == pygame.K_SPACE:
                char_2.punch()
            elif event.key == pygame.K_ENTER:
                char_1.punch()
        # -------------------------
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                char_1.moves.remove("right")
            elif event.key == pygame.K_UP:
                char_1.moves.remove("up")
            elif event.key == pygame.K_LEFT:
                char_1.moves.remove("left")
            elif event.key == pygame.K_DOWN:
                char_1.moves.remove("down")
            elif event.key == pygame.K_d:
                char_2.moves.remove("right")
            elif event.key == pygame.K_w:
                char_2.moves.remove("up")
            elif event.key == pygame.K_a:
                char_2.moves.remove("left")
            elif event.key == pygame.K_s:
                char_2.moves.remove("down")




    for character in characters:
        for direction in character.moves:
            character.move(direction)
        character.in_punch -= 1
        if character.in_punch <= 0:
            character.stage = 'stand'

    display.blit(background_image, [0, 0])
    char_1.show_img()
    char_2.show_img()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
