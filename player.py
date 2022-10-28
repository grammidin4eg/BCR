import pygame
from game_object import GameObject
from constants import *
from bullet import Bullet
from controls import isControlDown, isControlFire, isControlLeft, isControlRight, isControlUp

SPEED = 4
BULLET_DELAY = 500
COLLIDE_FIX = 3

def findPlayer(objects):
    for cur in objects:
        if cur.tag == 'Player':
            return cur
    return None

class Player(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('tank', x, y)
        self.speed = SPEED
        self.directX = 0
        self.directY = -1
        self.nextBulletThreshold = 0
        self.tag = 'Player'
        self.life = 3
        self.collideRect.width = self.collideRect.width - COLLIDE_FIX
        self.collideRect.x = self.collideRect.x - COLLIDE_FIX
        self.collideRect.height = self.collideRect.height - COLLIDE_FIX
        self.collideRect.y = self.collideRect.y - COLLIDE_FIX
    def update(self, events, objects):
        keys = pygame.key.get_pressed()
        directionX = 0
        directionY = 0
        if isControlUp():
            self.rotate(0)
            directionY = -1

        if isControlDown():
            self.rotate(180)
            directionY = 1

        if isControlRight():
            self.rotate(-90 - directionY * 45)
            directionX = 1

        if isControlLeft():
            self.rotate(90 + directionY * 45)
            directionX = -1
            
        if directionX != 0 or directionY != 0:
            self.directY = directionY
            self.directX = directionX
            self.move(directionX, directionY, objects, True)
        
        current_time = pygame.time.get_ticks()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if isControlFire(event) and current_time > self.nextBulletThreshold:
                    objects.add(Bullet(self.rect.centerx, self.rect.centery, self.directX, self.directY, self))
                    self.nextBulletThreshold = current_time + BULLET_DELAY

        return super().update(events, objects)