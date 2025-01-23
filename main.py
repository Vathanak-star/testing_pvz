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

#Load Assets
background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.png')).convert()
steve_backyard = pygame.image.load(os.path.join(images_dir, 'steve_house_background.jpg'))
pixel_background = pygame.image.load(os.path.join(images_dir, 'pixel_background.jpg'))
#resize the image
steve_backyard = pygame.transform.scale(steve_backyard, (800, 600))
pixel_background = pygame.transform.scale(pixel_background, (800, 600))
#convert_alpha = to remove the transparent background
zombie_image = pygame.image.load(os.path.join(images_dir, 'zombie_pvz.png')).convert_alpha()
#resize the image
zombie_image = pygame.transform.scale(zombie_image, (200,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(pixel_background,(0,0))
    x,y=pygame.mouse.get_pos()
    x-=zombie_image.get_width()/2
    y-=zombie_image.get_width()/2
    screen.blit(zombie_image,(x,y))
    pygame.display.update()