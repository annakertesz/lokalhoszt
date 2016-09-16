import pygame

class Char:

    def __init__ (self, x, y, width, height, direction, movestages, display, life=100):
        self.x = x
        self.y = y
        self.moves = []
        self.movestages = movestages
        self.stage = 'stand'
        self.life = life
        self.direction = direction
        self.rectbox = pygame.Rect(x, y, width, height)
        self.display = display

    def show_img(self):
        self.display.blit(self.movestages[self.stage], (self.x, self.y))

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
