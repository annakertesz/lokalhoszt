import pygame

class Char:

    def __init__ (self, filename, x, y):
        self.img = pygame.image.load(filename).convert_alpha()
        self.x = x
        self.y = y
        self.moves = []
        self.stages = {
            'stand': pygame.image.load('images/stand.png').convert_alpha(),
                       'crouch': pygame.image.load('images/crouch.png').convert_alpha(),
                       'jump': pygame.image.load('images/jump.png').convert_alpha(),
                       'kick': pygame.image.load('images/kick.png').convert_alpha(),
                       'punch': pygame.image.load('images/punch.png').convert_alpha(),
                       'block': pygame.image.load('images/block.png').convert_alpha()
        }
        self.stage = 'stand'

        self.life = life
        self.direction = direction
        self.movestages = movestages
        self.rectbox = rectbox


    def show_img(self, parent):
        parent.blit(self.stages[self.stage], (self.x, self.y))

    def move(self, direction):
        if direction == 'up':
            if self.y > 30:
                self.y -= 10
            else:
                self.y = 20

        if direction == 'right':
            if self.x < 1000:
                self.x += 10
            else:
                self.x = 1000

        if direction == 'left':
            if self.x > 30:
                self.x -= 10
            else:
                self.x = 20
        if direction == 'down':
            if self.y < 600:
                self.y += 10
            else:
                self.y = 600



    def move(self):
        pass

    def jump(self):
        pass

    def crouch(self):
        pass

    def punch(self):
        pass

    def block(self):
        pass

    def kick(self):
        pass

    def head(self):
        pass
