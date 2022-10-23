import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from level_loader import loadTestLevel
from player import Player
from block import Block, Block2

class GameStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.titleFont = pygame.font.Font('font1.ttf', 100)
        self.objects = loadTestLevel()
        self.ground = pygame.image.load(f'images/ground.png')
        # загрузка картинок
    def render(self, screen):
        # Заголовок
        # text = self.titleFont.render('GAME', 2, pygame.Color('blue'))
        # screen.blit(text, (200, 200))
        #screen.fill(pygame.Color('black')) # заливка экрана цветом
        for gx in range(4):
            for gy in range(3):
                screen.blit(self.ground, (gx * self.ground.get_rect().width, gy * self.ground.get_rect().height))
        self.objects.draw(screen)

    def update(self, events):
        self.objects.update(events, self.objects)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'