import pygame
import random
from game_object import SysObject
from enemy import createRandomEnemy

DEFAULT_TIME = 5000

class Portal(SysObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.delay = DEFAULT_TIME + random.randint(0, 2000)
        self.nextPortalThreshold = 0
        self.tag = 'Portal'
        self.count = 10
    def update(self, events, objects):
        if self.count < 1:
            return super().update(events, objects)
        current_time = pygame.time.get_ticks()
        if current_time > self.nextPortalThreshold:
            # проверим, нет ли коллизии сейчас с другими объектами
            for cur in objects:
                if cur.isMoveBlock and cur.collide(self.rect):
                    self.nextPortalThreshold = current_time + 200
                    return
            # создать объект
            objects.add(createRandomEnemy(self.rect.x, self.rect.y))
            self.count -= 1
            self.nextPortalThreshold = current_time + self.delay
        return super().update(events, objects)