import pygame
from first_char import Char

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


little_cube = Char(300, 300, 50, 50, "right", movestages, display)
another_cube = Char(800, 300, 50, 50, "right", movestages, display)

characters = [little_cube, another_cube]

#MAIN LOOP
game_over = False
while not game_over:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                little_cube.moves.append("right")
            if event.key == pygame.K_LEFT:
                little_cube.moves.append("left")
            if event.key == pygame.K_d:
                another_cube.moves.append("right")
            if event.key == pygame.K_a:
                another_cube.moves.append("left")
            if event.key == pygame.K_w:
                if another_cube.in_jump <= 0:
                    another_cube.in_jump = 50
            if event.key == pygame.K_UP:
                if little_cube.in_jump <= 0:
                    little_cube.in_jump = 50
        # -------------------------
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                little_cube.moves.remove("right")

            if event.key == pygame.K_LEFT:
                little_cube.moves.remove("left")
            if event.key == pygame.K_d:
                another_cube.moves.remove("right")
            if event.key == pygame.K_a:
                another_cube.moves.remove("left")

    for character in characters:
        if character.y < 400:
            character.stage = 'jump'
        else:
            character.stage = 'stand'
        character.jump()
        character.in_jump -= 1
        for direction in character.moves:
            character.move(direction)






    display.blit(background_image, [0, 0])

    little_cube.show_img()
    another_cube.show_img()
    pygame.display.update()

    clock.tick(60)


pygame.quit()
