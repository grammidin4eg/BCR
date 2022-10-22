import pygame
from pygame.constants import K_ESCAPE
from StageManagement import Stage
from constants import SCREEN_WIDTH

class EditorBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = 0
    def update(self, mousePos, curImage, index):
        if self.rect.collidepoint(mousePos):
            self.setIndex(index, curImage)
    def getIndex(self):
        return self.index
    def setIndex(self, index, img):
        self.index = index
        self.image = img

BS = 32
images = []
images.append(pygame.image.load(f'images/0.jpg'))
images.append(pygame.image.load(f'images/block1.png'))
images.append(pygame.image.load(f'images/block2.png'))
images.append(pygame.image.load(f'images/grass.png'))
images.append(pygame.image.load(f'images/water.png'))
images.append(pygame.image.load(f'images/lava.png'))
images.append(pygame.image.load(f'images/tank.png'))
images.append(pygame.image.load(f'images/enemy1.png'))
        
class ConstructStage(Stage):
    def __init__(self):
        super().__init__()
        # загрузка картинок
        self.blocks = pygame.sprite.Group()
        self.cur = 1
        for y in range(19):
            for x in range(25):
                self.blocks.add(EditorBlock(x*BS,y*BS,images[0]))
    def render(self, screen):
        self.blocks.draw(screen)
        screen.blit(images[self.cur], (SCREEN_WIDTH - BS, 0))
    def changeCur(self, delta: int):
        self.cur += delta
        if self.cur >= len(images):
            self.cur = 1
        if self.cur < 1:
            self.cur = len(images) - 1
    def update(self, events):
        mp = [-10,-10]
        button = 0
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'MENU'
            if event.type == pygame.MOUSEWHEEL:
                self.changeCur(event.y)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button < 4:
                mp = event.pos
                button = event.button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.changeCur(1)
                if event.key == pygame.K_DOWN:
                    self.changeCur(-1)
                if event.key == pygame.K_s and event.mod & pygame.KMOD_CTRL:
                    print('save file save.lvl...')
                    fp = open('save.lvl', 'w')
                    stext = ""
                    for block in self.blocks:
                        stext += str(block.getIndex())
                    fp.write(stext)
                    fp.close()
                    print('done')
                if event.key == pygame.K_l and event.mod & pygame.KMOD_CTRL:
                    print('load file save.lvl...')
                    fp = open('save.lvl', 'r')
                    stext = fp.readline()
                    fp.close()
                    print('read: ', stext)
                    j = 0
                    for block in self.blocks:
                        curIndex = int(stext[j])
                        curImage = images[curIndex]
                        block.setIndex(curIndex, curImage)
                        j += 1
                    print('done')
                if event.key == pygame.K_n and event.mod & pygame.KMOD_CTRL:
                    j = 0
                    for block in self.blocks:
                        curImage = images[0]
                        block.setIndex(0, images[0])
        if button == 2:
            self.blocks.update(mp, images[0], 0)
        else:
            self.blocks.update(mp, images[self.cur], self.cur)