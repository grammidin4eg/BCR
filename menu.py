import pygame
from pygame.constants import K_DOWN, K_RETURN, K_UP
from StageManagement import Stage

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
        self.rect.x = 250
        self.menu = 0

        self.scenes = ['NEW_GAME', 'CONSTRUCT', 'EXIT']
        self.ym = 500
    def render(self, screen):
        # Заголовок
        text = self.titleFont.render('Battle', 2, pygame.Color('red'))
        screen.blit(text, (100, self.ym))
        text = self.titleFont.render('City', 2, pygame.Color('red'))
        screen.blit(text, (200, self.ym + 100))
        # Пункты меню
        text = self.menuFont.render('Новая игра', 2, pygame.Color('white'))
        screen.blit(text, (300, self.ym + 240))
        text = self.menuFont.render('Редактор', 2, pygame.Color('white'))
        screen.blit(text, (300, self.ym + 300))
        text = self.menuFont.render('Выход', 2, pygame.Color('white'))
        screen.blit(text, (300, self.ym + 360))
        # Танк для выбора меню
        self.rect.y = 240 + self.ym + self.menu * 60
        screen.blit(self.tank, self.rect)


    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN and self.menu < 2:
                    self.menu += 1
                if event.key == K_UP and self.menu > 0:
                    self.menu -= 1
                if event.key == K_RETURN:
                    return self.scenes[self.menu]
        if self.ym > 100:
            self.ym -= 3