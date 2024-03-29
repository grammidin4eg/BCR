import pygame
import random
from bullet import Bullet
from game_object import GameObject
from player import findPlayer

BULLET_DELAY = 900
CORRECT_DELAY = 2000
    
class Enemy(GameObject):
    def __init__(self, name, x: int, y: int):
        super().__init__(name, x, y)
        self.life = 1
        self.randomDirection()
        self.nextBulletThreshold = 0
        self.speed = 1
        self.tag = 'Enemy'
        self.isShild = True
        self.shieldTick = 1
        self.correctDelay = CORRECT_DELAY
        self.correctThreshold = pygame.time.get_ticks() + self.correctDelay + random.randint(0, 2000)
    def iSeeAim(self, player):
        if player == None:
            return False
        if (self.directY != 0):
            first = (player.rect.centerx >= self.rect.x) and (player.rect.centerx <= self.rect.x + self.rect.width)
            if self.directY > 0:
                return first and (player.rect.y >= self.rect.y)
            if self.directY < 0:
                return first and (player.rect.y < self.rect.y)
        if (self.directX != 0):
            first = (player.rect.centery >= self.rect.y) and (player.rect.centery <= self.rect.y + self.rect.height)
            if self.directX > 0:
                return first and (player.rect.x >= self.rect.x)
            if self.directX < 0:
                return first and (player.rect.x < self.rect.x)
        return False
    def moveToDirection(self, objects):
        hasCollide = self.move(self.directX, self.directY, objects, True)
        if hasCollide:
            self.randomDirection()
    def gotoUp(self):
        self.rotate(0)
        self.directY = -1
        self.directX = 0
    def gotoDown(self):
        self.rotate(180)
        self.directY = 1
        self.directX = 0
    def gotoLeft(self):
        self.rotate(90)
        self.directY = 0
        self.directX = -1
    def gotoRight(self):
        self.rotate(-90)
        self.directY = 0
        self.directX = 1
    def randomDirection(self):
        rway = random.randint(1, 4)
        if rway == 1:
            self.gotoDown()
        if rway == 2:
            self.gotoUp()
        if rway == 3:
            self.gotoLeft()
        if rway == 4:
            self.gotoRight()
    def correctWay(self, player):
        if player == None:
            return
        divX = player.rect.x - self.rect.x
        divY = player.rect.y - self.rect.y
        if abs(divX) > abs(divY):
            if player.rect.x < self.rect.x:
                self.gotoLeft()
            else:
                self.gotoRight()
        else:
            if player.rect.y < self.rect.y:
                self.gotoUp()
            else:
                self.gotoDown()
        pass
    def update(self, events, objects):
        player = findPlayer(objects)
        current_time = pygame.time.get_ticks()
        if current_time > self.correctThreshold:
            self.correctWay(player)
            self.correctThreshold = current_time + self.correctDelay
        self.moveToDirection(objects)
        if self.iSeeAim(player) and current_time > self.nextBulletThreshold:
            objects.add(Bullet(self.rect.centerx, self.rect.centery, self.directX, self.directY, self))
            self.nextBulletThreshold = current_time + BULLET_DELAY
        return super().update(events, objects)

class SimpleEnemy(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__('enemy1', x, y)


class FastEnemy(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__('enemy2', x, y)
        self.speed = 3
        self.correctDelay = 1000


class TankEnemy(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__('enemy4', x, y)
        self.speed = 1
        self.correctDelay = 3000
        self.life = 3


def createRandomEnemy(x, y):
    rnd = random.randint(1, 6)
    if rnd == 1 or rnd == 2 or rnd == 3:
        return SimpleEnemy(x, y)
    if rnd == 4 or rnd == 5:
        return FastEnemy(x, y)
    if rnd == 6:
        return TankEnemy(x, y)