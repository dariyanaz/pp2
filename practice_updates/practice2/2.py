import pygame 
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('рисуем')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (100, 100, 200, 150))
    pygame.draw.circle(screen, BLUE, (400, 300), 60)
    pygame.display.flip()
pygame.quit()