import pygame
import sys

pygame.init()

# Размер окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ускорение в Pygame")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальные параметры
x = 100
y = 300
width = 50
height = 50

vel_x = 0  # скорость по x
accel_x = 0.5  # ускорение по x

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Увеличиваем скорость за счёт ускорения
    vel_x += accel_x

    # Изменяем позицию по скорости
    x += vel_x

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()

pygame.quit()
sys.exit()

#ускорение