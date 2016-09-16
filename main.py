import pygame
from first_char import Char

pygame.init()


#main settings
display = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('localhost')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

background_image = pygame.image.load("images/background.jpg").convert()

little_cube = Char('images/littlecube.png')

#MAIN LOOP
game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    little_cube.move()
    display.blit(background_image, [0, 0])




    #background

    little_cube.show_img(display)
    pygame.display.update()

    clock.tick(60)


pygame.quit()