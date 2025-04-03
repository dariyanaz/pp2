import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Тест событий")

running = True
while running:
    for event in pygame.event.get():
        print(event)  # Вывод всех событий в консоль

        if event.type == pygame.QUIT:
            running = False

pygame.quit()