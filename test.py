from pygame import *

try:

    joystick.init()
    joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]
    joysticks[0].init()
    joysticks[1].init()
    joystick1 = joysticks[0]
    joystick2 = joysticks[1]
    print('sikerült megcsinálni')
except IndexError:
    joystick = None
    joystick = None
while True:
    player1jx = joystick1.get_axis(0)
    player1jy = joystick2.get_axis(1)
    print(player1jx, player1jy)
