from pygame import *

try:

    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joysticks[0].init()
    joysticks[1].init()
    joystick1 = joysticks[0]
    joystick2 = joysticks[1]
    print('sikerült megcsinálni')
except IndexError:
    joystick = None
    joystick = None
while True:
    player1jx = joystick.get_axis(0)
    player1jy = joystick.get_axis(1)
    print(player1jx, player1jy)
