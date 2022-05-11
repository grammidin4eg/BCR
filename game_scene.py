import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from player import Player

class GameStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.titleFont = pygame.font.Font('font1.ttf', 100)
        self.objects = pygame.sprite.Group(Player())
        # загрузка картинок
    def render(self, screen):
        # Заголовок
        # text = self.titleFont.render('GAME', 2, pygame.Color('blue'))
        # screen.blit(text, (200, 200))
        self.objects.draw(screen)

    def update(self, events):
        self.objects.update()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'