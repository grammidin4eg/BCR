import pygame
def isControlLeft():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_LEFT] or keys[pygame.K_a]
def isControlRight():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_RIGHT] or keys[pygame.K_d]

def isControlUp():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_UP] or keys[pygame.K_w]

def isControlDown():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_DOWN] or keys[pygame.K_s]

def isControlFire(event):
    return event.key == pygame.K_SPACE