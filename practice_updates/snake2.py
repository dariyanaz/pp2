import pygame  
import random  

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 600  # Размер игрового поля (квадрат 600x600 пикселей)
CELL_SIZE = 20  # Размер одной клетки змейки и еды
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна игры
pygame.display.set_caption("Snake Game")  # Заголовок окна

# Загрузка и масштабирование изображения головы змейки
head1 = pygame.image.load('image.png')  # Загрузка изображения
head2 = pygame.transform.scale(head1, (CELL_SIZE, CELL_SIZE))  # Изменение размера под клетку

# Цвета для игры (RGB)
GREEN = (0, 200, 0)    # Цвет змейки
BLACK = (20, 20, 20)    # Цвет фона
RED = (255, 0, 0)       # Цвет еды
WHITE = (255, 255, 255) # Цвет текста
GREY = (40, 40, 40)     # Цвет сетки

# Настройка шрифта для отображения счета и уровня
font = pygame.font.Font(None, 36)  # Стандартный шрифт, размер 36px

# Класс змейки
class Snake:
    def __init__(self):
        # Начальное тело змейки - список координат сегментов
        self.body = [(100, 100), (80, 100)]  # Два сегмента, начальная позиция
        self.dx, self.dy = CELL_SIZE, 0  # Направление движения (начально вправо)
        self.alive = True  # Флаг жизни змейки

    def move(self):
        if not self.alive:  # Если змейка мертва, не двигаться
            return

        # Получаем координаты головы
        head_x, head_y = self.body[0]
        # Вычисляем новую позицию головы
        new_head = (head_x + self.dx, head_y + self.dy)
        # Отображаем изображение головы
        screen.blit(head2, (head_x, head_y))

        # Проверка столкновения со стенами
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.alive = False  # Змейка умирает при ударе о стену
            return

        # Проверка столкновения с собой
        if new_head in self.body:
            self.alive = False  # Змейка умирает при столкновении с собой
            return

        # Добавляем новую голову и удаляем хвост (движение)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        # Увеличение змейки (добавляем копию последнего сегмента)
        self.body.append(self.body[-1])

    def draw(self):
        # Отрисовка всех сегментов змейки
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE), border_radius=5)
            
    def draw_grid(self):
        # Отрисовка сетки игрового поля
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                pygame.draw.rect(screen, GREY, (x, y, CELL_SIZE, CELL_SIZE), 1)

# Класс еды
class Food:
    def __init__(self, snake_body):
        self.position = self.spawn_food(snake_body)  # Позиция еды
        self.weight = random.randint(1, 3)  # Вес еды (1-3)
        self.timer = random.randint(3, 7) * 1000  # Время жизни еды (3-7 секунд)
        self.spawn_time = pygame.time.get_ticks()  # Время появления еды

    def spawn_food(self, snake_body):
        # Генерация случайной позиции для еды
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            # Проверка, что еда не появится на змейке
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        # Отрисовка еды с закругленными углами
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE), border_radius=10)

    def has_expired(self):
        # Проверка, истекло ли время жизни еды
        return pygame.time.get_ticks() - self.spawn_time > self.timer

# Основной игровой цикл
running = True  # Флаг работы игры
snake = Snake()  # Создание змейки
food = Food(snake.body)  # Создание первой еды
clock = pygame.time.Clock()  # Объект для контроля FPS
score = 0  # Начальный счет
level = 1  # Начальный уровень
FPS = 10  # Начальная скорость игры (кадров в секунду)

while running:
    screen.fill(BLACK)  # Очистка экрана (заливка черным)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна
            running = False
        elif event.type == pygame.KEYDOWN:  # Нажатие клавиши
            # Управление змейкой с проверкой, чтобы нельзя было развернуться на 180°
            if event.key == pygame.K_LEFT and snake.dx == 0:  # Влево, если не движемся вправо
                snake.dx, snake.dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:  # Вправо, если не движемся влево
                snake.dx, snake.dy = CELL_SIZE, 0
            elif event.key == pygame.K_UP and snake.dy == 0:  # Вверх, если не движемся вниз
                snake.dx, snake.dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and snake.dy == 0:  # Вниз, если не движемся вверх
                snake.dx, snake.dy = 0, CELL_SIZE

    snake.move()  # Движение змейки

    # Проверка, съела ли змейка еду
    if snake.body[0] == food.position:
        for _ in range(food.weight):  # Увеличение змейки на величину веса еды
            snake.grow()
        score += food.weight  # Увеличение счета
        food = Food(snake.body)  # Создание новой еды

        # Повышение уровня каждые 5 очков
        if score % 5 == 0:
            level += 1
            FPS += 2  # Увеличение скорости игры

    # Проверка, не истекло ли время жизни еды
    if food.has_expired():
        food = Food(snake.body)  # Создание новой еды

    # Отрисовка игровых объектов
    snake.draw()  # Змейка
    food.draw()   # Еда
    snake.draw_grid()  # Сетка

    # Отображение счета и уровня
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Контроль скорости игры

    # Если змейка умерла, задержка перед выходом
    if not snake.alive:
        pygame.time.delay(1000)  # Пауза 1 секунда
        running = False  # Завершение игры

pygame.quit()  # Завершение работы Pygame