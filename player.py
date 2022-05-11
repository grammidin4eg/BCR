import pygame
from game_object import GameObject
from constants import *

SPEED = 4

class Player(GameObject):
    def __init__(self):
        super().__init__('tank', SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    def update(self):
        keys = pygame.key.get_pressed()
        directionX = 0
        directionY = 0
        if keys[pygame.K_UP]:
            self.rotate(0)
            directionY = -1
        if keys[pygame.K_DOWN]:
            self.rotate(180)
            directionY = 1

        if keys[pygame.K_RIGHT]:
            self.rotate(-90 - directionY * 45)
            directionX = 1
        if keys[pygame.K_LEFT]:
            self.rotate(90 + directionY * 45)
            directionX = -1
        #if directionX != 0:
        #    self.flip(directionX < 0)
        self.rect.x += directionX * SPEED
        self.rect.y += directionY * SPEED
        return super().update()