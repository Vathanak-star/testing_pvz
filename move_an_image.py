import pygame
import os
pygame.init()

win = pygame.display.set_mode((500,500))

base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')
images_dir = os.path.join(assets_dir, 'images')

background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.png')).convert()
background_image = pygame.transform.scale(background_image, (200,200))
rect = background_image.get_rect(center = (250//2,250//2))

moving = False
while True:
    win.fill('white')
    win.blit(background_image,rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
        if event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            moving = True
        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    pygame.display.update()

