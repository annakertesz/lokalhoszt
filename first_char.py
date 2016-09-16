import pygame

class Char:


    def __init__ (self, filename):
        self.img = pygame.image.load(filename).convert()
        self.x = 20
        self.y = 20


    def show_img(self, parent):
        parent.blit(self.img, (self.x, self.y))

    def move(self):
        self.x += 5
# if lenyomtad:
#     while not felemeled:
#         menjen balra
#             bla(dif 0 1)