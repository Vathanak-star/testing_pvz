import pygame
import os

pygame.init()

#Set up screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Plant Vs Zombie')


#Define Paths to the image
base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')
images_dir = os.path.join(assets_dir, 'images')

background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.png'))
background_image = pygame.transform.scale(background_image, (800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background_image,(0,0))
    pygame.display.update()

