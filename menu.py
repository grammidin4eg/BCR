import pygame
from StageManagement import Stage
from controls import isControlDown, isControlEnter, isControlUp
from utils import centerTextX
from constants import SCREEN_WIDTH

class MenuStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.titleFont = pygame.font.Font('font1.ttf', 100)
        self.menuFont = pygame.font.Font('font3.ttf', 34)
        # загрузка картинок
        self.tank = pygame.image.load('images/tank.png').convert_alpha()
        self.tank = pygame.transform.scale(self.tank, (40, 40))
        self.tank = pygame.transform.rotate(self.tank, -90)
        self.rect = self.tank.get_rect()
        self.menu = 0
        self.titleObj = self.titleFont.render('Battle', 2, pygame.Color('red'))
        self.subtitleObj = self.titleFont.render('City', 2, pygame.Color('red'))
        self.menu1 = self.menuFont.render('Новая игра', 2, pygame.Color('white'))
        self.menu2 = self.menuFont.render('Редактор', 2, pygame.Color('white'))
        self.menu3 = self.menuFont.render('Выход', 2, pygame.Color('white'))
        self.rect.x = centerTextX(self.menu1) - 70

        self.scenes = ['NEW_GAME', 'CONSTRUCT', 'EXIT']
        self.ym = 500
    def render(self, screen):
        # Заголовок
        screen.blit(self.titleObj, (centerTextX(self.titleObj), self.ym))
        screen.blit(self.subtitleObj, (centerTextX(self.subtitleObj), self.ym + 100))
        # Пункты меню
        screen.blit(self.menu1, (centerTextX(self.menu1), self.ym + 240))
        screen.blit(self.menu2, (centerTextX(self.menu1), self.ym + 300))
        screen.blit(self.menu3, (centerTextX(self.menu1), self.ym + 360))
        # Танк для выбора меню
        self.rect.y = 240 + self.ym + self.menu * 60
        screen.blit(self.tank, self.rect)


    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if isControlDown(event) and self.menu < 2:
                    self.menu += 1
                if isControlUp(event) and self.menu > 0:
                    self.menu -= 1
                if isControlEnter(event):
                    return self.scenes[self.menu]
        if self.ym > 100:
            self.ym -= 3