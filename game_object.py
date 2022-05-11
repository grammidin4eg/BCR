import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, file_name: str, x: int, y: int):
        super().__init__()
        self.image = self.origin = pygame.image.load(f'images/{file_name}.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        pass
    def collide(self, rect):
        return self.rect.colliderect(rect)
    def rotate(self, angle: int):
        self.image = pygame.transform.rotate(self.origin, angle)