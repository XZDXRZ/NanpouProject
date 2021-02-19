import pygame, os

pygame.init()

gamescreen = pygame.display.set_mode([756, 535])
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