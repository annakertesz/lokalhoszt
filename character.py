import pygame


class Character:

    def __init__(self, x, y,  direction, movestages, display, width=70, height=380, life=100):
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
        self.in_head = 0
        self.in_kick = 0
        self.blockpower = 10000
        self.in_punch = 0
        self.opponent = None

    def show_img(self):
        if self.direction == 'left':
            self.display.blit(pygame.transform.flip(self.movestages[self.stage], True, False), (self.x, self.y))
        else:
            self.display.blit(self.movestages[self.stage], (self.x, self.y))

    def move(self, direction):

        if direction == 'right':
            if self.x < 1000:
                self.x += 10
            else:
                self.x = 1000
            self. direction = 'right'

        if direction == 'left':
            if self.x > 30:
                self.x -= 10
            else:
                self.x = 20
            self.direction = 'left'

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
        self.jump()
        self.in_jump -= 1

    def crouch(self):
        if self.crouch_stage is True:
            self.stage = 'crouch'

    def punch(self):
        if self.direction == 'right':
            punch_rect = pygame.Rect(self.x + self.body_width, self.y + self.from_head_shoulder_level,
                                     self.arm_length, self.arm_height)
        else:
            punch_rect = pygame.Rect(self.x - self.body_width, self.y + self.from_head_shoulder_level,
                                     self.arm_length, self.arm_height)
        opponent_rectbox = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if self.in_punch <= 0:
            self.in_punch = 30
            self.stage = 'punch'
            self.show_img()
        if opponent_rectbox.colliderect(punch_rect):
            if self.opponent.stage != 'block':
                self.opponent.life -= 11
            elif self.opponent.direction == self.direction:
                self.opponent.life -= 11

    def block(self):
        self.stage = 'block'

    def block_out(self):
        self.stage = 'stand'

    def kick(self):
        if self.direction == 'right':
            kick_rect = pygame.Rect(self.x + self.body_width, self.y + self.from_head_shoulder_level,
                                    self.arm_length, self.arm_height)
        else:
            kick_rect = pygame.Rect(self.x - self.body_width, self.y + self.from_head_shoulder_level,
                                    self.arm_length, self.arm_height)
        opponent_rectbox = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if self.in_kick <= 0:
            self.in_kick = 20
            self.stage = 'kick'
            self.show_img()

        if opponent_rectbox.colliderect(kick_rect):
            if self.opponent.stage != 'block':
                self.opponent.life -= 11
            elif self.opponent.direction == self.direction:
                self.opponent.life -= 11

    def head(self):
        if self.direction == 'right':
            head_rect = pygame.Rect(self.x + self.body_width/2, self.y + self.from_head_shoulder_level-30,
                                    self.arm_length, self.arm_height)
        else:
            head_rect = pygame.Rect(self.x - self.body_width, self.y + self.from_head_shoulder_level,
                                    self.arm_length, self.arm_height)
        opponent_rectbox = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if self.in_head <= 0:
            self.in_head = 10
            self.stage = 'head'
            self.show_img()

        if opponent_rectbox.colliderect(head_rect):
            x_push = 100
            if self.direction == 'left':
                x_push = - 100
            self.opponent.x += x_push
            if self.opponent.stage != 'block':
                self.opponent.life -= 11
            elif self.opponent.direction == self.direction:
                self.opponent.life -= 11
