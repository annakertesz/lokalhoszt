import pygame

class Char:


    def __init__ (self, filename, direction, movestages, rectbox, life=100):
        self.img = pygame.image.load(filename).convert()
        self.x = 20
        self.y = 20
        self.life = life
        self.direction = direction
        self.movestages = movestages
        self.rectbox = rectbox


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
