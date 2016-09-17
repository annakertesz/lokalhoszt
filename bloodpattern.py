import random
import pygame


class BloodPattern():

    bps = []

    @classmethod
    def add_pattern(cls, number_of_patterns, picture):

        list_of_patterns = []
        for pattern in range(number_of_patterns):
            list_of_patterns.append([picture, [random.randint(250, 850), random.randint(250, 750)]])
        BloodPattern(list_of_patterns)

    def __init__(self, list_of_patterns):

        self.duration = 100
        self.patterns = list_of_patterns
        self.__class__.bps.append(self)
