import pygame
from enum import Enum

imageHash = {}

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