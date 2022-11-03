from numpy import array
import pygame

MARGIN = 20

def renderMenus(array, screen):
    activeMenu = None
    for menu in array:
        menu.render(screen)
        if menu.active:
            activeMenu = menu
    return activeMenu


class RectMenu:
    def __init__(self, text, rect, font, active=False):
        self.rect = rect
        self.active = active
        self.obj = font.render(text, 1, pygame.Color('white'))
        self.left = None
        self.right = None
        self.up = None
        self.down = None
    def goTo(self, toMenu):
        if toMenu:
            toMenu.active = True
            self.active = False
    def render(self, screen):
        screen.blit(self.obj, (self.rect.x + MARGIN, self.rect.y + MARGIN))
        color = pygame.Color('green') if self.active else pygame.Color('white')
        pygame.draw.rect(screen, color, self.rect, 2)
    def update(self):
        pass