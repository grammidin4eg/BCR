import pygame
from game_object import GameObject
from constants import BS
from block import Block, Block2, Water, Grass, Lava
from player import Player
from enemy import Enemy
from ground import setCurGround

def loadTestLevel() -> pygame.sprite.Group:
    return loadLevelByFullName('save.lvl')


# images.append(pygame.image.load(f'images/0.jpg')) - 0
# images.append(pygame.image.load(f'images/block1.png')) - 1
# images.append(pygame.image.load(f'images/block2.png')) - 2
# images.append(pygame.image.load(f'images/grass.png')) - 3
# images.append(pygame.image.load(f'images/water.png')) - 4
# images.append(pygame.image.load(f'images/lava.png')) - 5
# images.append(pygame.image.load(f'images/tank.png')) - 6
# images.append(pygame.image.load(f'images/enemy1.png')) - 7


def loadLevelByFullName(file_name: str) -> pygame.sprite.Group:
    objects = pygame.sprite.Group()
    print('load file {0}...'.format(str))
    fp = open(file_name, 'r')
    stext = fp.readline()
    fp.close()
    print('read: ', stext)
    setCurGround(int(stext[0]))
    j = 1
    # создаем массив
    for y in range(19):
        for x in range(25):
            newObj = None
            newX = x*BS
            newY = y*BS
            if stext[j] == '1':
                newObj = Block(newX, newY)
            if stext[j] == '2':
                newObj = Block2(newX, newY)
            if stext[j] == '3':
                newObj = Grass(newX, newY)
            if stext[j] == '4':
                newObj = Water(newX, newY)
            if stext[j] == '5':
                newObj = Lava(newX, newY)
            if stext[j] == '6':
                newObj = Player(newX, newY)
            if stext[j] == '7':
                newObj = Enemy(newX, newY)
            if stext[j] == '8':
                newObj = GameObject('portal', newX, newY)
            if newObj != None:
                objects.add(newObj)
                print('add ', newObj)
            j += 1
        
    print('done')
    return objects