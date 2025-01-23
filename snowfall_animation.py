import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((400,400))
snow = []

for i in range(50):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
    snow.append([x,y])

clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if(events.type == pygame.QUIT):
            pygame.quit()
            quit()
    
    screen.fill('white')
    for ice in range(len(snow)):
        pygame.draw.circle(screen,'sky blue',snow[ice],3)
        snow[ice][1]+=1
        if snow[ice][1] > 400:
            snow[ice][1] = random.randrange(-50,-10)
            snow[ice][0] = random.randrange(0,400)
    pygame.display.update()
    clock.tick(40)