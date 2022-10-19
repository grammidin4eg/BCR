import pygame
from game_object import GameObject

class Block(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('block1', x, y)
        self.life = 3
    def update(self, events, objects):
        return super().update()
    

class Block2(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('block2', x, y)
        self.life = 1000
    def update(self, events, objects):
        return super().update()