import pygame
from StageManagement import Stage
from ui_elements import RectMenu, renderMenus
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class NewGameScene(Stage):
    def __init__(self):
        super().__init__()
        self.titleFont = pygame.font.Font('font1.ttf', 70)
        self.titleObj = self.titleFont.render('New battle', 2, pygame.Color('red'))
        self.secondFont = pygame.font.Font('font3.ttf', 28)
        self.secondObj = self.secondFont.render('Choose second ability:', 1, pygame.Color('white'))
        self.menus = []
        abil1 = RectMenu('Blink', pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, 50), self.secondFont, True)
        goMenu = RectMenu('GO!', pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT - 50, 100, 50), self.secondFont, True)
        abil1.down = goMenu
        goMenu.up = abil1
        self.menus.append(abil1)
        self.menus.append(goMenu)
        self.activeMenu = None
    def render(self, screen):
        screen.blit(self.titleObj, (50, 120))
        screen.blit(self.secondObj , (50, 230))
        self.activeMenu = renderMenus(self.menus, screen)
    def update(self, events):
        pass
    def start(self):
        pass