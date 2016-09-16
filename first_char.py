import pygame

class Char:

    def __init__ (self, filename, x, y):
        self.img = pygame.image.load(filename).convert()
        self.x = x
        self.y = y
        self.moves = []


    def show_img(self, parent):
        parent.blit(self.img, (self.x, self.y))

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
