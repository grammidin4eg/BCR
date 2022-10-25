import pygame
import glob
import math

def showAnimation(name, pos, objects):
    for curObj in objects:
        if curObj.tag == 'animation' and curObj.folder == name:
            curObj.start(pos)
            break

def showBoom(pos, objects):
    anim = AnimationSprite('explosion', 0.3)
    objects.add(anim)
    anim.start(pos)

class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, folder, speed=1, loop=False):
        super().__init__()
        self.images = [pygame.image.load(img) for img in glob.glob("images/" + folder + "/*.png")]
        self.index = 0
        self.rect = self.images[0].get_rect()
        self.speed = speed
        self.tick = 0
        self.isAnimated = False
        self.isLoop = loop
        self.tag = 'animation'
        self.isMoveBlock = False
        self.isAim = False
        self.image = pygame.image.load('images/null.png').convert_alpha()
        self.folder = folder
    def start(self, pos):
        self.rect = self.images[0].get_rect(center = pos)
        self.animated(True)
    def animated(self, isAnimated):
        self.tick = 0
        self.isAnimated = isAnimated
    def update(self, events, objects):
        if self.isAnimated:
            if self.tick >= len(self.images):
                if not self.isLoop:
                    self.kill()
                    return
                self.tick = 0
            self.index = math.floor(self.tick)
            self.image = self.images[self.index]
            self.tick += self.speed