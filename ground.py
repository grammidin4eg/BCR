import pygame

images = [pygame.image.load(f"images/ground/{index}.png") for index in range(1, 6)]

GROUND_LEN = len(images) - 1

curGround = {'value': 0}
def setCurGround(index: int):
    curGround['value'] = index

def renderGround(screen, groundIndex = -1):
    if groundIndex == -1:
        groundIndex = curGround['value']
    ground = images[groundIndex]
    for gx in range(4):
        for gy in range(3):
            screen.blit(ground, (gx * ground.get_rect().width, gy * ground.get_rect().height))