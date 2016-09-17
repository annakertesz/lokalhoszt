import pygame
import random
from sounds import *


class Character:

    def __init__(self, x, y,  direction, movestages, display, width=150, height=280, life=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body_width = 150
        self.from_head_shoulder_level = 130
        self.arm_length = 135
        self.arm_height = 35
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
        self.won = 0
        self.joystick = None

    def show_img(self):
        if self.direction == 'left':
            self.display.blit(pygame.transform.flip(self.movestages[self.stage], True, False), (self.x, self.y))
        else:
            self.display.blit(self.movestages[self.stage], (self.x, self.y))

    def checking_overlaping(self):
        body_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        opponent_body_rect = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if opponent_body_rect.colliderect(body_rect):
            if self.direction == 'left' and self.opponent.direction == 'right':
                self.opponent.x -= 11
            elif self.direction == 'right' and self.opponent.direction == 'left':
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

        if direction == 'down':
            if self.y < 600:
                self.y += 10
            else:
                self.y = 600

    def jump(self):
        if self.in_jump > 20:
            self.y -= int(self.in_jump / 3)
        elif self.y < 400:
            self.crouch_stage = False
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
        if self.in_punch <= -30 and self.in_kick <= -30 and self.in_head <= -30:
            self.in_punch = 30
            random_hit = [sound['hit1'], sound['hit2'], sound['hit3'], sound['hit4'], sound['hit5']]
            random.choice(random_hit).play()
            self.stage = 'punch'
            self.show_img()
            if opponent_rectbox.colliderect(punch_rect):
                dmg = random.randint(1, 99)
                if self.opponent.stage != 'block':
                    self.opponent.life -= dmg
                elif self.opponent.direction == self.direction:
                    self.opponent.life -= dmg
                x_push = int(200 * dmg/100)
                if self.direction == 'left':
                    x_push = - x_push
            else:
                sound['swing'].play()

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
        if self.in_punch <= -30 and self.in_kick <= -30 and self.in_head <= -30:
            self.in_kick = 20
            self.stage = 'kick'
            self.show_img()
            if opponent_rectbox.colliderect(kick_rect):
                dmg = random.randint(1, 99)
                if self.opponent.stage != 'block':
                    random_kick = [sound['kick1'], sound['kick2'], sound['kick3'], sound['kick4']]
                    random.choice(random_kick).play()
                    self.opponent.life -= dmg
                elif self.opponent.direction == self.direction:
                    random_kick = [sound['kick1'], sound['kick2'], sound['kick3'], sound['kick4']]
                    random.choice(random_kick).play()
                    self.opponent.life -= dmg
                x_push = int(200 * dmg/100)
                if self.direction == 'left':
                    x_push = - x_push
            else:
                sound['empty_kick'].play()


    def head(self):
        if self.direction == 'right':
            head_rect = pygame.Rect(self.x + self.body_width/2, self.y + self.from_head_shoulder_level-30,
                                    self.arm_length, self.arm_height)
        else:
            head_rect = pygame.Rect(self.x - self.body_width, self.y + self.from_head_shoulder_level,
                                    self.arm_length, self.arm_height)
        opponent_rectbox = pygame.Rect(self.opponent.x, self.opponent.y, self.opponent.width, self.opponent.height)
        if self.in_punch <= -30 and self.in_kick <= -30 and self.in_head <= -30:
            self.in_head = 10
            self.stage = 'head'
            self.show_img()

            if opponent_rectbox.colliderect(head_rect):
                dmg = random.randint(1, 99)
                if self.opponent.stage != 'block':
                    sound['headbutt'].play()
                    self.opponent.life -= dmg
                elif self.opponent.direction == self.direction:
                    sound['headbutt'].play()
                    self.opponent.life -= dmg
                x_push = int(200 * dmg/100)
                if self.direction == 'left':
                    x_push = - x_push
                self.opponent.x += x_push
            else:
                sound['swing'].play()
