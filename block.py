import pygame
from game_object import GameObject

class Block(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('block1', x, y)
        self.life = 3
    def update(self, events, objects):
        return super().update(events, objects)
    

class Block2(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('block2', x, y)
        self.life = 1000
    def update(self, events, objects):
        return super().update(events, objects)

class Water(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('water', x, y)
        self.life = 1000
        self.isAim = False
    def update(self, events, objects):
        return super().update(events, objects)

class Grass(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('grass', x, y)
        self.life = 1000
        self.isAim = False
        self.isMoveBlock = False
    def update(self, events, objects):
        return super().update(events, objects)
    
class Lava(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__('lava', x, y)
        self.life = 1000
        self.isAim = False
        self.isMoveBlock = False
    def update(self, events, objects):
        for curObj in objects:
            if (curObj.tag == 'Player' or curObj.tag == 'Enemy') and curObj.collide(self.rect):
                curObj.killThis(objects)
        return super().update(events, objects)