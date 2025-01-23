import pygame
import random
pygame.init()

screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('Color breezing')

clock = pygame.time.Clock()
c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)

def reset():
    global c1,c2,c3
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse Clicked')
            reset()
    
    if 0<c1<255:
        c1 += 1
    elif c1>255:
        c1 -= 255
    elif c1<=0:
        c1 +=3

    clock.tick(100)

    screen.fill((c1,c2,c3))

    pygame.display.update()

