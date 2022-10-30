import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from game_object import UIObject
from ground import renderGround
from level_loader import loadTestLevel
from anim_sprite import AnimationSprite
from player import findPlayer

class GameStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.uiFont = pygame.font.Font('font1.ttf', 16)
        self.objects = loadTestLevel()
        self.ground = pygame.image.load(f'images/ground.png')
        self.player = findPlayer(self.objects)
        self.objects.add(UIObject('heart', 10, 10))
        # загрузка картинок
    def render(self, screen):
        renderGround(screen)
        self.objects.draw(screen)
        # вторичная отрисовка объектов
        for curObj in self.objects:
            if curObj.isMoveBlock:
                curObj.secondDraw(screen)
        # UI
        # жизни
        text = self.uiFont.render(str(self.player.life), 2, pygame.Color('orange'))
        screen.blit(text, (37, 13))

    def update(self, events):
        self.objects.update(events, self.objects)
        #проверим, жив ли игрок. Если нет - game over
        if self.player.life < 1:
            return 'GAMEOVER'
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'