import math
import random


class Particle:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

        angle = random.uniform(0, 2*math.pi)

        self.vx = math.cos(angle)*2
        self.vy = math.sin(angle)*2