import pygame;
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('pygame text!')
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)

font.set_underline(True)
text = font.render("Hello Everyone!",True,(255,255,255))
textrect = text.get_rect()
textrect.center = ((500//2, 500//2))

while True:
    screen.fill((131,37,97))
    screen.blit(text, textrect)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        pygame.display.update()