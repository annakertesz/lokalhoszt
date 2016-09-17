import pygame
from pygame.locals import *

pygame.init()

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.locals.JOYAXISMOTION:
            player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
            if player1jx < 0:
                print("left")
            if player1jx > 0:
                print("right")
            if player1jy < 0:
                print("up")
            if player1jy > 0:
                print("down")