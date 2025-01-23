import pygame
import os
pygame.init()

win = pygame.display.set_mode((500,500))

base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')
images_dir = os.path.join(assets_dir, 'images')

background_image = pygame.image.load(os.path.join(images_dir, 'pvz_background.png')).convert()
background_image = pygame.transform.scale(background_image, (200,200))

i=0

while True:
    if i>500:
        i=0
        pygame.time.wait(500)

    win.fill('white')

    win.blit(background_image,(i,0))
    #(i,0) mean move stright , (0,i) mean move down
    i += 80
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.time.wait(500)