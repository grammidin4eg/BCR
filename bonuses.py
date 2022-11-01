import pygame
import random
from game_object import BonusObject
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BS

class LifeBonus(BonusObject):
    def __init__(self, x: int, y: int):
        super().__init__('bonuslife', x, y)
    def takeBonus(self, player, objects):
        player.life += 1
        return super().takeBonus(player, objects)

class ShildBonus(BonusObject):
    def __init__(self, x: int, y: int):
        super().__init__('bonushelm', x, y)
    def takeBonus(self, player, objects):
        player.giveShield()
        return super().takeBonus(player, objects)

def createRandomBonus(objects):
    # если бонусов уже 3 и более, то не создаем новый
    bonuses = 0
    for cur in objects:
        if cur.tag == 'BonusObject':
            bonuses += 1
    if bonuses >= 3:
        return False
    # определить пустое место
    x = random.randrange(0, SCREEN_WIDTH - BS, BS)
    y = random.randrange(0, SCREEN_HEIGHT - BS, BS)
    for cur in objects:
        if cur.isMoveBlock and cur.collide(pygame.Rect(x, y, BS, BS)):
            return createRandomBonus(objects)
    # вернуть случайный бонус
    rnd = random.randint(1, 2)
    if rnd == 1:
        objects.add(LifeBonus(x, y))
    if rnd == 2:
        objects.add(ShildBonus(x, y))
    return True