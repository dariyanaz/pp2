import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('обработка событий')

WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Go')
            if event.key == pygame.K_s:
                print('back')
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f'click: {event.pos}, knopka: {event.button}')
            
    screen.fill(WHITE)

    
    pygame.display.flip()
    
pygame.quit()