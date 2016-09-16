import pygame

class Character:

    def __init__(self, x, y,  direction, movestages, display, width=70, height=150, life=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body_width = 55
        self.from_head_shoulder_level = 105
        self.arm_length = 130
        self.arm_height = 5
        self.moves = []
        self.movestages = movestages
        self.stage = 'stand'
        self.life = life
        self.direction = direction
        self.display = display
        self.in_jump = 0
        self.crouch_stage = False
        self.in_punch = 0
        self.opponent = None

    def show_img(self):
        if self.direction == 'left':
            self.display.blit(pygame.transform.flip(self.movestages[self.stage], True, False), (self.x, self.y))
        else:
            self.display.blit(self.movestages[self.stage], (self.x, self.y))

    def checking_overlaping(self):
        body_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        opponent_body_rect = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if opponent_body_rect.colliderect(body_rect):
            if self.direction == 'left':
                self.opponent.x -= 11
            elif self.direction == 'right':
                self.opponent.x += 11

    def space_limit(self):
        if self.x > 1000:
            self.x = 1000
        elif self.x < 0:
            self.x = 0
        if self.y > 600:
            self.y = 600
        elif self.y < 0:
            self.y = 0

    def move(self, direction):
        if direction == 'right':
            self.x += 10
            self.direction = 'right'
        elif direction == 'left':
            self.x -= 10
            self.direction = 'left'

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
        # else:
        #     self.stage = 'stand'
        self.jump()
        self.in_jump -= 1



    def crouch(self):
        if self.crouch_stage == True:
            self.stage = 'crouch'
        # else:
        #     self.stage = 'stand'

    def punch(self):
        if self.direction == 'right':
            punch_rect = pygame.Rect(self.x + self.body_width, self.y + self.from_head_shoulder_level,
                                     self.arm_length, self.arm_height)
        else:
            punch_rect = pygame.Rect(self.x - self.body_width, self.y + self.from_head_shoulder_level,
                                     self.arm_length, self.arm_height)
        opponent_rectbox = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if self.in_punch <= 0:
            self.in_punch = 10
            self.stage = 'punch'
            self.show_img()
        if opponent_rectbox.colliderect(punch_rect):
            self.opponent.life -= 5
            print("üt")

    def block(self):
        pass

    def kick(self):
        pass

    def head(self):
        pass
