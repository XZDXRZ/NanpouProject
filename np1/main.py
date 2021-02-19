import pygame, os

pygame.init()
size = (756, 535)
tick = 10

MAXENERMY = 3
MAXENERMYSPEED = 10
MAXPLAYERBULLET = 100
PLAYERBULLETDELAY = 100
MAXENERMYBULLET = 7
ENERMYBULLETDELAY = 500

class Player(pygame.sprite.Sprite):
    def __init__(self):
        img = pygame.imame.load("./img/player/plane_1.png")


gamescreen = pygame.display.set_mode(size)
running = True
pygame.display.set_caption("np1")
bg_img = pygame.image.load("./img/bg_img.jpg")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gamescreen.blit(bg_img,[0,0])

    pygame.display.flip()

pygame.quit()