import pygame
from StageManagement import StageManager
from menu import MenuStage
from game_scene import GameStage
from construct import ConstructStage
from new_scene import NewGameScene
from constants import *

#Инициализация
FPS = 60

pygame.init()
#Создать экран определенного разрешения
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Задать заголовок окна
pygame.display.set_caption("Battle City Rogulike")
process = True

clock = pygame.time.Clock()

sceneManager = StageManager()
sceneManager.add(MenuStage(), 'MENU')
sceneManager.add(GameStage(), 'GAME')
sceneManager.add(ConstructStage(), 'CONSTRUCT')
sceneManager.add(NewGameScene(), 'NEW_GAME')
sceneManager.goTo('MENU')
#Основной цикл игры
while process:
    # обработка событий игры
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            process = False
    # Обновление игровых объектов
    if sceneManager.update(events) == 'EXIT':
        process = False
    # Отрисовка объектов на экране
    screen.fill(pygame.Color('black')) # заливка экрана цветом
    sceneManager.render(screen)
    # Обновление экрана и ожидание фреймов FPS
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()