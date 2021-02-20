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
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.imame.load("./img/player/plane_1.png")
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = (size[0]/2, size[1]/5*4)
        self.mask = pygame.mask.from_surface(self.img)
    
    #def move(self):

screen = pygame.display.set_mode(size)
running = True
pygame.display.set_caption("np1")
bg_img = pygame.image.load("./img/bg_img.jpg")
st_img = pygame.image.load("./img/st_img.jpg")
press_any_key_to_start = pygame.font.SysFont('Tiems', 40).render("Press any key to start...", True, (0,100,0))

# Start Image
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            running = False
    screen.blit(st_img,[0, 0])
    screen.blit(press_any_key_to_start, (size[0]/4, size[1]/2))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_img,[0,0])

    pygame.display.flip()

pygame.quit()