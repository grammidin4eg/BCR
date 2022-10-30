import pygame
from enum import Enum
from anim_sprite import showBoom
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

imageHash = {}

SHIELD_TICK_DELAY = 500

class GameObject(pygame.sprite.Sprite):
    def __init__(self, file_name: str, x: int, y: int):
        super().__init__()
        if (not imageHash.get(file_name)):
            imageHash[file_name] = pygame.image.load(
                f'images/{file_name}.png').convert_alpha()
        self.image = self.origin = imageHash[file_name]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collideRect = self.rect
        self.speed = 0
        self.life = 1
        self.isAim = True
        self.isMoveBlock = True
        self.tag = 'GameObject'
        self.angle = 0
        self.isShild = False
        self.shieldTick = 5
        self.isShildVisible = True
        self.shieldThreshold = pygame.time.get_ticks() + SHIELD_TICK_DELAY

    def update(self, events, objects):
        if self.isShild:
            current_time = pygame.time.get_ticks()
            if current_time > self.shieldThreshold:
                self.isShildVisible = not self.isShildVisible
                self.shieldTick -= 1
                self.shieldThreshold = current_time + SHIELD_TICK_DELAY
                if self.shieldTick < 1:
                    self.isShild = False
                    self.shieldTick = 5
                    self.isShildVisible = True
        pass

    def giveShield(self):
        self.isShild = True
        self.shieldTick = 5
        self.isShildVisible = True

    def secondDraw(self, surface):
        if self.isShild and self.isShildVisible:
            pygame.draw.circle(surface, pygame.Color('blue'), self.rect.center, 28, 3)

    def collide(self, rect):
        return self.collideRect.colliderect(rect)

    def rotate(self, angle: int):
        self.image = pygame.transform.rotate(self.origin, angle)
        self.angle = angle

    def move(self, moveX: int, moveY: int, objects = pygame.sprite.Group(), checkOutside = False):
        oldX = self.rect.x
        oldY = self.rect.y
        self.rect.x += moveX * self.speed
        self.rect.y += moveY * self.speed
        hasCollide = False
        for curObj in objects:
            if curObj != self and curObj.isMoveBlock and curObj.collide(self.rect):
                hasCollide = True
                break
        if checkOutside and self.isOutside():
            hasCollide = True
        if hasCollide:
            self.rect.x = oldX
            self.rect.y = oldY
        return hasCollide
    def isOutside(self) -> bool:
        return self.rect.x < 0 or (self.rect.x + self.rect.width) > SCREEN_WIDTH or self.rect.y < 0 or (self.rect.y + self.rect.height) > SCREEN_HEIGHT
    def hit(self, power: int, objects) -> int:
        if self.isShild:
            return self.life
        self.life -= power
        if self.life < 1:
            self.killThis(objects)
        elif self.tag == 'Player':
            self.giveShield()
        return self.life
    def getPos(self):
        return (self.rect.x, self.rect.y)
    def killThis(self, objects):
        showBoom(self.rect.center, objects)
        self.life = 0
        self.kill()


class UIObject(GameObject):
    def __init__(self, file_name: str, x: int, y: int):
        super().__init__(file_name, x, y)
        self.isAim = False
        self.isMoveBlock = False
        self.tag = 'UIObject'

class SysObject(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('null', x, y)
        self.isAim = False
        self.isMoveBlock = False
        self.tag = 'SysObject'