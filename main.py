import pygame
from first_char import Char

pygame.init()


#main settings
display = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('localhost')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

background_image = pygame.image.load("images/background.jpg").convert()

little_cube = Char('images/littlecube.png', 20, 20)
another_cube = Char('images/littlecube.png', 50, 50)

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
            if event.key == pygame.K_UP:
                little_cube.moves.append("up")
            if event.key == pygame.K_LEFT:
                little_cube.moves.append("left")
            if event.key == pygame.K_DOWN:
                little_cube.moves.append("down")
            if event.key == pygame.K_d:
                another_cube.moves.append("right")
            if event.key == pygame.K_w:
                another_cube.moves.append("up")
            if event.key == pygame.K_a:
                another_cube.moves.append("left")
            if event.key == pygame.K_s:
                another_cube.moves.append("down")
        # -------------------------
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                little_cube.moves.remove("right")
            if event.key == pygame.K_UP:
                little_cube.moves.remove("up")
            if event.key == pygame.K_LEFT:
                little_cube.moves.remove("left")
            if event.key == pygame.K_DOWN:
                little_cube.moves.remove("down")
            if event.key == pygame.K_d:
                another_cube.moves.remove("right")
            if event.key == pygame.K_w:
                another_cube.moves.remove("up")
            if event.key == pygame.K_a:
                another_cube.moves.remove("left")
            if event.key == pygame.K_s:
                another_cube.moves.remove("down")


    for character in characters:
        for direction in character.moves:
            character.move(direction)

    display.blit(background_image, [0, 0])

    little_cube.show_img(display)
    another_cube.show_img(display)
    pygame.display.update()

    clock.tick(60)


pygame.quit()
