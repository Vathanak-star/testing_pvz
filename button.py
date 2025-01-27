import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame Button')

font = pygame.font.SysFont('tahoma',40,bold=True)
surf = font.render('Quit', True,'white')
button = pygame.Rect(200,200,110,60)

while True:
    screen.fill('pink')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                pygame.quit()
                quit()
    x,y = pygame.mouse.get_pos()
    if button.x <= x <= button.x + 110 and button.y <= y <= button.y + 60:
        pygame.draw.rect(screen,(180,180,180),button)
    else:
        pygame.draw.rect(screen, (110,110,110),button)
    screen.blit(surf,(button.x + 5, button.y + 5))
    pygame.display.update()