import pygame
from enum import Enum
from anim_sprite import showBoom
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

imageHash = {}


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

    def update(self, events, objects):
        pass

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
        self.life -= power
        if self.life < 1:
            self.killThis(objects)
        return self.life
    def getPos(self):
        return (self.rect.x, self.rect.y)
    def killThis(self, objects):
        showBoom(self.rect.center, objects)
        self.kill()


class UIObject(GameObject):
    def __init__(self, file_name: str, x: int, y: int):
        super().__init__(file_name, x, y)
        self.isAim = False
        self.isMoveBlock = False
        self.tag = 'UIObject'