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
        self.in_jump = 0

    def show_img(self):
        self.display.blit(self.movestages[self.stage], (self.x, self.y))

    def move(self, direction):

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

        if self.in_jump > 20:
            self.y -= int(self.in_jump / 3)
        elif self.y < 400:
            self.y += int((25-self.in_jump)/1.5)
        elif self.y == 400:
            self.stage = 'stand'

    def jump_step(self):
        if self.y < 400:
            self.stage = 'jump'
        else:
            self.stage = 'stand'
        self.jump()
        self.in_jump -= 1



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
