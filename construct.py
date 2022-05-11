import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage

class ConstructStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.titleFont = pygame.font.Font('font1.ttf', 60)
        # загрузка картинок
    def render(self, screen):
        # Заголовок
        text = self.titleFont.render('CONSTRUCT', 2, pygame.Color('blue'))
        screen.blit(text, (100, 200))

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'