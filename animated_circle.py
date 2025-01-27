import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('animated circle')

x,y = 200,200
xv = 5
yv = 0
clock = pygame.time.Clock()


while True:
    screen.fill('sky blue')
    pygame.draw.circle(screen, 'green',(x,y),10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    x += xv
    y += yv

    if x>490 or x<10:
        xv *= -1
    if y>490 or y<10:
        yv *= -1

    pygame.display.update()
    clock.tick(100)