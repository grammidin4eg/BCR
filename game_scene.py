import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from player import Player
from block import Block, Block2

class GameStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.titleFont = pygame.font.Font('font1.ttf', 100)
        self.objects = pygame.sprite.Group(Player())
        self.objects.add(Block2(380, 20))
        self.objects.add(Block(340, 30))
        # загрузка картинок
    def render(self, screen):
        # Заголовок
        # text = self.titleFont.render('GAME', 2, pygame.Color('blue'))
        # screen.blit(text, (200, 200))
        self.objects.draw(screen)

    def update(self, events):
        self.objects.update(events, self.objects)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'