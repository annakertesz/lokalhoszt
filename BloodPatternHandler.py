import random

class BloodPatternHandler():

    patterns = []

    def __init__(self):

        self.coordinates = [random.randint(100, 700), random.randint(100, 700)]
        self.remaining_time = 1000
        self.__class__.patterns.append(self)
