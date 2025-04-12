import pygame
import random
import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="12345678"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s", (user_id,))
    data = cur.fetchone()

    if data:
        score, level = data
    else:
        cur.execute("INSERT INTO user_scores (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        score, level = 0, 1

    cur.close()
    conn.close()
    return user_id, score, level

def save_state(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE user_scores SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)

def input_username():
    username = ""
    active = True
    input_box = pygame.Rect(150, 250, 300, 50)
    color_active = pygame.Color('lightskyblue3')

    while active:
        screen.fill(BLACK)
        txt_surface = font.render("Введите имя: " + username, True, WHITE)
        pygame.draw.rect(screen, color_active, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip() != "":
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

    return username.strip()

class Level:
    def __init__(self, number):
        self.number = number
        self.walls = self.generate_walls()

    def generate_walls(self):
        walls = []
        if self.number == 2:
            for i in range(0, WIDTH, CELL_SIZE):
                walls.append((i, 200))
        elif self.number == 3:
            for i in range(0, HEIGHT, CELL_SIZE):
                walls.append((300, i))
        elif self.number == 4:
            for i in range(0, WIDTH, CELL_SIZE):
                if i % 40 == 0:
                    for j in range(0, HEIGHT, CELL_SIZE):
                        walls.append((i, j))
        return walls

    def draw(self):
        for wall in self.walls:
            pygame.draw.rect(screen, WHITE, (*wall, CELL_SIZE, CELL_SIZE))

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100)]
        self.dx, self.dy = CELL_SIZE, 0
        self.alive = True

    def move(self, walls):
        if not self.alive:
            return

        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)

        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.alive = False
            return

        if new_head in self.body or new_head in walls:
            self.alive = False
            return

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body, walls):
        self.position = self.spawn_food(snake_body, walls)
        self.weight = random.randint(1, 3)
        self.timer = random.randint(3, 7) * 1000
        self.spawn_time = pygame.time.get_ticks()

    def spawn_food(self, snake_body, walls):
        while True:
            x = random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE
            y = random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE
            if (x, y) not in snake_body and (x, y) not in walls:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

    def has_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.timer

'''   
def show_high_level():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT users.username, user_scores.level FROM user_scores JOIN users ON user_scores.user_id = users.id WHERE user_scores.level>1;')
    rows = cur.fetchall()
    print('\nигроки с уровнем выше 1:')
    for row in rows:
        print(f'name: {row[0]}, level: {row[1]}')
        
    cur.close()
    conn.close()
    
show_high_level()
'''
    

# GAME START
create_tables()
username = input_username()
user_id, score, level = get_or_create_user(username)

print(f"Добро пожаловать, {username}. Ваш текущий уровень: {level}")

snake = Snake()
level_obj = Level(level)
food = Food(snake.body, level_obj.walls)
clock = pygame.time.Clock()
FPS = 10 + (level - 1) * 2
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = CELL_SIZE, 0
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, CELL_SIZE
            elif event.key == pygame.K_p:
                save_state(user_id, score, level)
                paused = True
                pause_text = font.render("Пауза. Нажмите P чтобы продолжить.", True, WHITE)
                screen.blit(pause_text, (60, HEIGHT // 2))
                pygame.display.flip()
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                            paused = False

    snake.move(level_obj.walls)

    if snake.body[0] == food.position:
        for _ in range(food.weight):
            snake.grow()
        score += food.weight
        if score % 5 == 0:
            level += 1
            FPS = 10 + (level - 1) * 2
            level_obj = Level(level)
            print(f"Поздравляем! Новый уровень: {level}")
        food = Food(snake.body, level_obj.walls)

    if food.has_expired():
        food = Food(snake.body, level_obj.walls)

    level_obj.draw()
    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

    if not snake.alive:
        pygame.time.delay(1000)
        save_state(user_id, score, level)
        running = False

pygame.quit()
