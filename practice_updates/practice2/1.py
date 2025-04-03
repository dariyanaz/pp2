import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("game")

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
# This code initializes a Pygame window and runs a loop that keeps the window open until the user closes it.