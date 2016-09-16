import pygame

class Lifebar:

    def __init__(self, display, char, x, y):
        self.x = x
        self.y = y
        self.life = char.life
        self.display = display

    def show(self):

        if self.life > 90:
            self.display.blit(pygame.image.load('images/lifebar_10.png').convert_alpha(), (self.x, self.y))
        elif self.life > 80 and self.life < 90:
            self.display.blit(pygame.image.load('images/lifebar_9.png').convert_alpha(), (self.x, self.y))
        elif self.life > 70 and self.life < 80:
            self.display.blit(pygame.image.load('images/lifebar_8.png').convert_alpha(), (self.x, self.y))
        elif self.life > 60 and self.life < 70:
            self.display.blit(pygame.image.load('images/lifebar_7.png').convert_alpha(), (self.x, self.y))
        elif self.life > 50 and self.life < 60:
            self.display.blit(pygame.image.load('images/lifebar_6.png').convert_alpha(), (self.x, self.y))
        elif self.life > 40 and self.life < 50:
            self.display.blit(pygame.image.load('images/lifebar_5.png').convert_alpha(), (self.x, self.y))
        elif self.life > 30 and self.life < 40:
            self.display.blit(pygame.image.load('images/lifebar_4.png').convert_alpha(), (self.x, self.y))
        elif self.life > 20 and self.life < 30:
            self.display.blit(pygame.image.load('images/lifebar_3.png').convert_alpha(), (self.x, self.y))
        elif self.life > 10 and self.life < 20:
            self.display.blit(pygame.image.load('images/lifebar_2.png').convert_alpha(), (self.x, self.y))
        elif self.life > 1 and self.life < 10:
            self.display.blit(pygame.image.load('images/lifebar_1.png').convert_alpha(), (self.x, self.y))