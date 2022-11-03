import pygame
from StageManagement import Stage
from controls import isControlDown, isControlLeft, isControlRight, isControlUp
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
        abil1 = RectMenu('Blink', pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, 50), self.secondFont)
        abil2 = RectMenu('Blink 2', pygame.Rect(SCREEN_WIDTH/2 + 100, SCREEN_HEIGHT/2, 100, 50), self.secondFont)
        abil3 = RectMenu('Blink 3', pygame.Rect(SCREEN_WIDTH/2 + 200, SCREEN_HEIGHT/2, 100, 50), self.secondFont)
        goMenu = RectMenu('GO!', pygame.Rect(SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT - 100, 100, 70), self.secondFont, True)
        abil1.down = goMenu
        abil2.down = goMenu
        abil3.down = goMenu
        goMenu.up = abil1
        abil1.right = abil2
        abil2.left = abil1
        abil2.right = abil3
        abil3.left = abil2
        self.menus.append(abil1)
        self.menus.append(abil2)
        self.menus.append(abil3)
        self.menus.append(goMenu)
        self.activeMenu = None
    def render(self, screen):
        screen.blit(self.titleObj, (50, 120))
        screen.blit(self.secondObj , (50, 230))
        self.activeMenu = renderMenus(self.menus, screen)
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if isControlUp(event):
                    self.activeMenu.goTo(self.activeMenu.up)
                if isControlDown(event):
                    self.activeMenu.goTo(self.activeMenu.down)
                if isControlLeft(event):
                    self.activeMenu.goTo(self.activeMenu.left)
                if isControlRight(event):
                    self.activeMenu.goTo(self.activeMenu.right)
    def start(self):
        pass