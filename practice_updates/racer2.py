import pygame, sys  # Основная библиотека и модуль для выхода
from pygame.locals import *  # Импорт констант Pygame
import random, time  # Для случайных чисел и задержки времени

# Инициализация всех модулей Pygame
pygame.init()

# Загрузка фонового изображения (должен существовать файл 'background.png')
background = pygame.image.load('background.png')

# Определение цветов в формате RGB (Red, Green, Blue)
BLACK = (0, 0, 0)  # Черный цвет
RED = (255, 0, 0)  # Красный цвет

# Настройка шрифтов для текста в игре
font = pygame.font.SysFont("Verdana", 60)  # Крупный шрифт (60px)
font_small = pygame.font.SysFont("Verdana", 20)  # Мелкий шрифт (20px)
# Создание текстовой поверхности с надписью "Game Over"
game_over = font.render("Game Over", True, BLACK)

# Получение размеров окна из размеров фонового изображения
WIDTH, HEIGHT = background.get_size()
# Создание главного окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установка заголовка окна
pygame.display.set_caption("Car game")

# Игровые переменные:
SPEED = 5  # Начальная скорость движения врагов
SCORE = 0  # Счет игрока (за избегание машин)
COINS_COLLECTED = 0  # Количество собранных монет
COINS_FOR_SPEEDUP = 10  # Необходимое количество монет для ускорения
clock = pygame.time.Clock()  # Объект для контроля частоты кадров

# Класс игрока (автомобиль игрока)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса
        self.image = pygame.image.load('Player.png')  # Загрузка изображения
        self.rect = self.image.get_rect()  # Получение прямоугольника объекта
        # Начальная позиция игрока (центр по X, снизу экрана)
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def update(self):
        """Обновление позиции игрока на основе нажатых клавиш"""
        pressed_keys = pygame.key.get_pressed()  # Получаем состояние клавиш
        # Движение влево (клавиша A) с проверкой границы
        if self.rect.left > 140 and pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)  # Изменяем позицию
        # Движение вправо (клавиша D) с проверкой границы
        if self.rect.right < 700 and pressed_keys[pygame.K_d]:
            self.rect.move_ip(5, 0)  # Изменяем позицию

# Класс врага (автомобили-препятствия)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса
        self.image = pygame.image.load('Enemy.png')  # Загрузка изображения
        self.rect = self.image.get_rect()  # Получение прямоугольника объекта
        # Случайная начальная позиция вверху экрана
        self.rect.center = (random.randint(40, WIDTH - 140), 0)

    def move(self):
        """Движение врага вниз по экрану"""
        global SCORE  # Используем глобальную переменную счета
        self.rect.move_ip(0, SPEED)  # Движение вниз с текущей скоростью
        # Если враг достиг нижней границы экрана
        if self.rect.bottom > HEIGHT:
            SCORE += 1  # Увеличиваем счет
            self.rect.top = 0  # Возвращаем в верх экрана
            # Новая случайная позиция по горизонтали
            self.rect.center = (random.randint(140, WIDTH - 140), 0)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса
        self.image = pygame.image.load('Coin.png')  # Загрузка изображения
        # Уменьшение размера монеты
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()  # Получение прямоугольника объекта
        self.reset_position()  # Установка начальной позиции и значения

    def reset_position(self):
        """Сброс позиции монеты и установка случайного значения"""
        # Случайная позиция вверху экрана (за пределами видимости)
        self.rect.center = (random.randint(140, WIDTH - 140), random.randint(-100, -40))
        # Случайное значение монеты (1, 2 или 5)
        self.value = random.choice([1, 2, 5])

    def move(self):
        """Движение монеты вниз (медленнее врагов)"""
        self.rect.move_ip(0, SPEED // 2)  # Движение с половинной скоростью
        # Если монета ушла за нижнюю границу
        if self.rect.top > HEIGHT:
            self.reset_position()  # Сброс позиции

# Создание экземпляра игрока
P1 = Player()
# Создание экземпляра врага
E1 = Enemy()

# Создание групп спрайтов:
enemies = pygame.sprite.Group()  # Группа для врагов
enemies.add(E1)  # Добавление врага в группу

coins = pygame.sprite.Group()  # Группа для монет
# Создание одной монеты (можно увеличить количество)
for _ in range(1):
    coins.add(Coin())

all_sprites = pygame.sprite.Group()  # Группа для всех спрайтов
all_sprites.add(P1)  # Добавление игрока
all_sprites.add(E1)  # Добавление врага

# Создание пользовательского события для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
# Установка таймера - событие будет происходить каждую секунду (1000 мс)
pygame.time.set_timer(INC_SPEED, 1000)

# Главный игровой цикл
running = True
while running:
    # Отрисовка фона (первый слой)
    screen.blit(background, (0, 0))

    # Обработка всех событий
    for event in pygame.event.get():
        # Обработка события увеличения скорости
        if event.type == INC_SPEED:
            SPEED += 0.2  # Небольшое увеличение скорости
        # Обработка события закрытия окна
        if event.type == pygame.QUIT:
            running = False  # Выход из цикла

    # Отрисовка и обновление всех спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)  # Отрисовка
        # Для врагов вызываем move(), для игрока - update()
        if isinstance(entity, Enemy):
            entity.move()
        else:
            entity.update()

    # Обработка монет
    for coin in coins:
        screen.blit(coin.image, coin.rect)  # Отрисовка
        coin.move()  # Движение

        # Проверка столкновения игрока с монетой
        if pygame.sprite.collide_rect(P1, coin):
            COINS_COLLECTED += coin.value  # Увеличение счета монет
            coin.reset_position()  # Сброс монеты

            # Проверка набора достаточного количества монет для ускорения
            if COINS_COLLECTED % COINS_FOR_SPEEDUP == 0:
                SPEED += 1  # Значительное увеличение скорости

    # Отрисовка счета (количество избежаных машин)
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))

    # Отрисовка количества собранных монет
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(coins_text, (WIDTH - 120, 10))

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)  # Заливка экрана красным
        screen.blit(game_over, (WIDTH//2 - 170, HEIGHT//2 - 30))  # "Game Over"
        pygame.display.update()  # Обновление экрана
        time.sleep(2)  # Пауза 2 секунды
        running = False  # Завершение игры

    # Обновление экрана
    pygame.display.update()
    # Ограничение частоты кадров (60 FPS)
    FPS = 60
    clock.tick(FPS)

# Завершение работы Pygame
pygame.quit()
# Выход из программы
sys.exit()