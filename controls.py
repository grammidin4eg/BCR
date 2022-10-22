import pygame
def isControlLeft():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_LEFT] or keys[pygame.K_a]
def isControlRight():
    pass