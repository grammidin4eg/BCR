import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game_object import GameObject
SPEED = 10

class Bullet(GameObject):
    def __init__(self, x: int, y: int, moveX: int, moveY: int):
        super().__init__('Bullet', x, y)
        self.speed = SPEED
        self.directionX = moveX
        self.directionY = moveY
    def update(self, events, objects):
        self.move(self.directionX, self.directionY)
        if self.rect.x < 0 or self.rect.y > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()
        return super().update()