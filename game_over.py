import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from constants import SCREEN_HEIGHT

class GameOverStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.titleFont = pygame.font.Font('font1.ttf', 84)
        self.titleObject = self.titleFont.render('Game Over', 2, pygame.Color('red'))

        self.subtitleFont = pygame.font.Font('font3.ttf', 26)
        self.subtitleObject = self.subtitleFont.render('Press ECS for exit', 2, pygame.Color('orange'))
        # загрузка картинок
    def render(self, screen):
        # заголовок
        screen.blit(self.titleObject, (30, SCREEN_HEIGHT/2 - 62))
        screen.blit(self.subtitleObject, (260, SCREEN_HEIGHT/2 + 26))

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'