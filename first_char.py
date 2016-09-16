import pygame

class Char:


    def __init__ (self, filename):
        self.img = pygame.image.load(filename).convert()
        self.x = 20
        self.y = 20
        self.moves = []


    def show_img(self, parent):
        parent.blit(self.img, (self.x, self.y))

    def move(self, direction):
        if direction == 'up':
            self.y -= 10
        if direction == 'right':
            self.x += 10
        if direction == 'left':
            self.x -= 10
        if direction == 'down':
            self.y += 10
