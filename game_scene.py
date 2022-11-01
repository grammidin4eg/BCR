import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from bonuses import createRandomBonus
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game_object import UIObject
from ground import renderGround
from level_loader import loadTestLevel
from anim_sprite import AnimationSprite
from player import findPlayer

BONUS_EVENT = pygame.USEREVENT

class GameStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка шрифта
        self.uiFont = pygame.font.Font('font1.ttf', 16)
        self.titleFont = pygame.font.Font('font1.ttf', 84)
        
        self.titleObject = self.titleFont.render('Game Over', 2, pygame.Color('red'))
        self.subtitleFont = pygame.font.Font('font3.ttf', 26)
        self.subtitleObject = self.subtitleFont.render('Press Esc for exit', 2, pygame.Color('orange'))
        
        self.uiObjects = pygame.sprite.Group()
        self.uiObjects.add(UIObject('heart', 10, 10))
        self.uiObjects.add(UIObject('uialiens', SCREEN_WIDTH - 80, 10))
        pygame.time.set_timer(BONUS_EVENT, 7000)
        # загрузка картинок
    def start(self):
        self.objects = loadTestLevel()
        self.player = findPlayer(self.objects)
        self.isGameOver = False
    def render(self, screen):
        renderGround(screen)
        self.objects.draw(screen)
        # вторичная отрисовка объектов
        # заодно подсчитаем кол-во врагов
        aliens = 0
        for curObj in self.objects:
            if curObj.isMoveBlock:
                curObj.secondDraw(screen)
            if curObj.tag == 'Enemy':
                aliens += 1
            if curObj.tag == 'Portal':
                aliens += curObj.count
        # UI
        self.uiObjects.draw(screen)
        # жизни
        text = self.uiFont.render(str(self.player.life), 2, pygame.Color('orange'))
        screen.blit(text, (37, 14))
        # враги
        text = self.uiFont.render(str(aliens), 2, pygame.Color('orange'))
        screen.blit(text, (SCREEN_WIDTH - 50, 14))
        
        #game over
        if self.isGameOver:
            pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(0, SCREEN_HEIGHT/2 - 80, SCREEN_WIDTH, 150))
            screen.blit(self.titleObject, (30, SCREEN_HEIGHT/2 - 62))
            screen.blit(self.subtitleObject, (260, SCREEN_HEIGHT/2 + 26))

    def update(self, events):
        self.objects.update(events, self.objects)
        #проверим, жив ли игрок. Если нет - game over
        if self.player.life < 1:
            #return 'GAMEOVER'
            self.isGameOver = True
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'
            if event.type == BONUS_EVENT:
                createRandomBonus(self.objects)