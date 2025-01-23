import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
font = pygame.font.SysFont('timesnewroman', 30)
letter = font.render('Pygame', False,'orange')
i=0

while True:
    if i>500:
        i=0
        pygame.time.wait(500)

    win.fill('white')

    win.blit(letter,(0,i))
    #(i,0) mean move stright , (0,i) mean move down
    i += 80
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.time.wait(500)


