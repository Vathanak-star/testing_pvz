import pygame
import os

pygame.init()

#Set up screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame with Assets')


#Define Paths to the image
base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')
images_dir = os.path.join(assets_dir, 'images')

#Load Assets
background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.png')).convert()
#convert_alpha = to remove the transparent background
steve_backyard = pygame.image.load(os.path.join(images_dir, 'steve_house_background.jpg'))
steve_backyard = pygame.transform.scale(steve_backyard, (800, 600))
zombie_image = pygame.image.load(os.path.join(images_dir, 'zombie_pvz.png')).convert_alpha() 
#resize the image
zombie_image = pygame.transform.scale(zombie_image, (200,200))

x,y = 0,0
move_x,move_y = 0,0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -1
            elif event.key == pygame.K_RIGHT:
                move_x = +1
            elif event.key == pygame.K_UP:
                move_y = -1
            elif event.key == pygame.K_DOWN:
                move_y= +1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_x = 0
            elif event.key == pygame.K_RIGHT:
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y= 0
    x += move_x
    y += move_y

    screen.fill((0,0,0))
    screen.blit(zombie_image,(x,y))
    pygame.display.update()
