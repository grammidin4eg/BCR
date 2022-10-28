import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game_object import GameObject
SPEED = 7

class Bullet(GameObject):
    def __init__(self, x: int, y: int, moveX: int, moveY: int, owner: GameObject):
        super().__init__('Bullet', x, y)
        self.speed = SPEED
        self.directionX = moveX
        self.directionY = moveY
        self.owner = owner
        self.power = 1
    def update(self, events, objects):
        self.move(self.directionX, self.directionY)
        if self.isOutside():
            self.kill()
        for obj in objects:
            if obj.isAim == True and obj != self and obj != self.owner and obj.collide(self.rect):
                obj.hit(self.power, objects)
                self.kill()
                break
        return super().update(events, objects)