import pygame
from game_object import Direction, GameObject
from constants import *
from bullet import Bullet

SPEED = 4

class Player(GameObject):
    def __init__(self):
        super().__init__('tank', SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.speed = SPEED
        self.direct = Direction.EMPTY
    def update(self, events, objects):
        keys = pygame.key.get_pressed()
        directionX = 0
        directionY = 0
        if keys[pygame.K_UP]:
            self.rotate(0)
            directionY = -1
            self.direct = Direction.UP
        if keys[pygame.K_DOWN]:
            self.rotate(180)
            directionY = 1
            self.direct = Direction.DOWN

        if keys[pygame.K_RIGHT]:
            self.rotate(-90 - directionY * 45)
            directionX = 1
            self.direct = Direction.RIGHT
        if keys[pygame.K_LEFT]:
            self.rotate(90 + directionY * 45)
            directionX = -1
            self.direct = Direction.LEFT
        #if directionX != 0:
        #    self.flip(directionX < 0)
        self.rect.x += directionX * self.speed
        self.rect.y += directionY * self.speed

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    objects.add(Bullet(self.rect.centerx, self.rect.centery, self.direct))

        return super().update()