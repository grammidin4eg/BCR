import pygame
from game_object import GameObject
from constants import *
from bullet import Bullet
from controls import isControlLeft

SPEED = 4
BULLET_DELAY = 500

class Player(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('tank', x, y)
        self.speed = SPEED
        self.directX = 0
        self.directY = -1
        self.nextBulletThreshold = 0
    def update(self, events, objects):
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

        if isControlLeft():
            self.rotate(90 + directionY * 45)
            directionX = -1
            
        if directionX != 0 or directionY != 0:
            self.directY = directionY
            self.directX = directionX
        #if directionX != 0:
        #    self.flip(directionX < 0)
        self.move(directionX, directionY)
        
        
        current_time = pygame.time.get_ticks()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and current_time > self.nextBulletThreshold:
                    objects.add(Bullet(self.rect.centerx, self.rect.centery, self.directX, self.directY, self))
                    self.nextBulletThreshold = current_time + BULLET_DELAY

        return super().update(events, objects)