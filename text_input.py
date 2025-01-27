import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('user input')

user_input = ''
font =  pygame.font.SysFont('tahoma', 40)
text_box = pygame.Rect(75,75,100,50)
active = False
color = pygame.Color('purple')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
    
    screen.fill('blue')
    if active:
        color = pygame.Color('red')
    else:
        color = pygame.Color('purple')
    pygame.draw.rect(screen,color,text_box,4)
    surf = font.render(user_input,True,'orange')
    screen.blit(surf, (text_box.x +5, text_box.y +5))
    text_box.w = max(100, surf.get_width()+10)
    pygame.display.update()
    clock.tick(50)