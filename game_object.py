import pygame
from enum import Enum

imageHash = {}

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    EMPTY = 0


class GameObject(pygame.sprite.Sprite):
    def __init__(self, file_name: str, x: int, y: int):
        super().__init__()
        if (not imageHash.get(file_name)):
            print('load image: ', file_name)
            imageHash[file_name] = pygame.image.load(f'images/{file_name}.png').convert_alpha()
        self.image = self.origin = imageHash[file_name]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
    def update(self):
        pass
    def collide(self, rect):
        return self.rect.colliderect(rect)
    def rotate(self, angle: int):
        self.image = pygame.transform.rotate(self.origin, angle)
    def move(self, moveX: int, moveY: int):
        self.rect.x += moveX * self.speed
        self.rect.y += moveY * self.speed
    def moveDirection(self, direction: Direction):
        moveX = 0
        moveY = 0
        if direction == Direction.RIGHT:
            moveX = 1
        if direction == Direction.LEFT:
            moveX = -1
        if direction == Direction.UP:
            moveY = -1
        if direction == Direction.DOWN:
            moveY = 1
        self.move(moveX, moveY)