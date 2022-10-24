import pygame
from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('enemy1', x, y)
        self.life = 1
    def update(self, events, objects):
        return super().update(events, objects)