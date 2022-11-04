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

def isControlLeft(event):
    return event.key == pygame.K_LEFT or event.key == pygame.K_a

def isControlRight(event):
    return event.key == pygame.K_RIGHT or event.key == pygame.K_d

def isControlUp(event):
    return event.key == pygame.K_UP or event.key == pygame.K_w

def isControlDown(event):
    return event.key == pygame.K_DOWN or event.key == pygame.K_s

def isControlEnter(event):
    return event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER