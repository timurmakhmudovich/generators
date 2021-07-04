import random


class RandomDigit():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __str__(self):
        return str(self.gen())

    def gen(self):
        return random.randrange(self.min, self.max + 1)


a = RandomDigit(1, 10)

print(a, a, a, a, a)
