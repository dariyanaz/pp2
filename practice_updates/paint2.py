import pygame
import pygame.gfxdraw  # Для дополнительных графических функций (например, заливки)


WIDTH, HEIGHT = 800, 600  
# Цвета в формате RGB:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Режимы инструментов (для удобства использования)
BRUSH = "brush"        # Кисть
ERASER = "eraser"      # Ластик
RECTANGLE = "rectangle" # Прямоугольник
CIRCLE = "circle"      # Окружность
SQUARE = "square"      # Квадрат
TRIANGLE = "triangle"  # Треугольник
EQUILATERAL = "equilateral"  # Равносторонний треугольник
RHOMBUS = "rhombus"    # Ромб
LINE = "line"          # Линия
FILL = "fill"          # Заливка

def main():
    pygame.init()
    # Создание окна с указанными размерами
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Установка заголовка окна
    pygame.display.set_caption("Paint")
    
    # Создание поверхности для рисования (холст)
    canvas = pygame.Surface((WIDTH, HEIGHT))
    # Заливка холста белым цветом
    canvas.fill(WHITE)
    
    # Настройки рисования
    colors = [BLACK, RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, CYAN]  # Доступные цвета
    color = BLACK  # Текущий цвет
    drawing = False  # Флаг рисования (нажата ли кнопка мыши)
    start_pos = None  # Начальная позиция рисования
    radius = 5  # Толщина кисти/ластика
    running = True  # Флаг работы программы
    mode = BRUSH  # Текущий режим рисования
    fill = False  # Режим заливки фигур
    
    # Система отмены действий
    undo_stack = []  # Стек для хранения состояний холста
    max_undo = 10  # Максимальное количество отмен
    
    # Создание объекта для контроля FPS
    clock = pygame.time.Clock()
    
    def save_state():
        """Сохраняет текущее состояние холста в стек отмены"""
        if len(undo_stack) >= max_undo:
            undo_stack.pop(0)  # Удаляем самое старое состояние, если достигли максимума
        undo_stack.append(canvas.copy())  # Сохраняем копию холста
    
    def undo():
        """Отменяет последнее действие, восстанавливая предыдущее состояние холста"""
        if undo_stack:
            canvas.blit(undo_stack.pop(), (0, 0))  # Восстанавливаем последнее сохраненное состояние
    
    # Главный цикл программы
    while running:
        # Отрисовка холста на экране
        screen.blit(canvas, (0, 0))
        
        # Отображение информации о текущих настройках
        font = pygame.font.SysFont(None, 24)
        # Создаем текстовые поверхности с информацией:
        tool_text = font.render(f"Tool: {mode}", True, BLACK)
        color_text = font.render(f"Color: {color}", True, BLACK)
        size_text = font.render(f"Size: {radius}", True, BLACK)
        # Отображаем текст в левом верхнем углу:
        screen.blit(tool_text, (10, 10))
        screen.blit(color_text, (10, 40))
        screen.blit(size_text, (10, 70))
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Завершение программы при закрытии окна

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                # Смена инструментов
                if event.key == pygame.K_r:
                    mode = RECTANGLE
                elif event.key == pygame.K_c:
                    mode = CIRCLE
                elif event.key == pygame.K_b:
                    mode = BRUSH
                elif event.key == pygame.K_e:
                    mode = ERASER
                elif event.key == pygame.K_s:
                    mode = SQUARE
                elif event.key == pygame.K_t:
                    mode = TRIANGLE
                elif event.key == pygame.K_q:
                    mode = EQUILATERAL
                elif event.key == pygame.K_d:
                    mode = RHOMBUS
                elif event.key == pygame.K_l:
                    mode = LINE
                elif event.key == pygame.K_u:
                    undo()  # Отмена последнего действия
                elif event.key == pygame.K_SPACE:
                    fill = not fill  # Переключение режима заливки

                # Выбор цвета цифрами 1-8
                if pygame.K_1 <= event.key <= pygame.K_8:
                    color = colors[event.key - pygame.K_1]

                # Изменение размера кисти
                if event.key == pygame.K_DOWN and radius > 3:
                    radius -= 2
                if event.key == pygame.K_UP and radius < 30:
                    radius += 2

            # Обработка нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == FILL:
                    # Режим заливки (используется алгоритм flood fill)
                    save_state()
                    # Определяем цвет заливки (основной цвет или белый для правой кнопки)
                    fill_color = color if event.button == 1 else WHITE
                    # Выполняем заливку
                    pygame.gfxdraw.flood_fill(canvas, event.pos[0], event.pos[1], fill_color)
                else:
                    # Для других инструментов начинаем рисование
                    drawing = True
                    start_pos = event.pos
                    save_state()  # Сохраняем состояние перед изменением

            # Обработка отпускания кнопки мыши
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing and mode not in [BRUSH, ERASER, FILL]:
                    # Завершаем рисование фигур (кроме кисти и ластика)
                    end_pos = event.pos
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    
                    # Вычисляем параметры фигуры
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)
                    min_x = min(x1, x2)
                    min_y = min(y1, y2)
                    
                    # Рисуем фигуру в зависимости от выбранного режима
                    if mode == RECTANGLE:
                        if fill:
                            pygame.draw.rect(canvas, color, (min_x, min_y, width, height))
                        else:
                            pygame.draw.rect(canvas, color, (min_x, min_y, width, height), radius)
                    elif mode == CIRCLE:
                        radius_circle = int((width**2 + height**2)**0.5) // 2
                        center = ((x1 + x2) // 2, (y1 + y2) // 2)
                        if fill:
                            pygame.draw.circle(canvas, color, center, radius_circle)
                        else:
                            pygame.draw.circle(canvas, color, center, radius_circle, radius)
                    elif mode == SQUARE:
                        side = min(width, height)
                        if fill:
                            pygame.draw.rect(canvas, color, (x1, y1, side, side))
                        else:
                            pygame.draw.rect(canvas, color, (x1, y1, side, side), radius)
                    elif mode == TRIANGLE:
                        points = [(x1, y2), (x2, y2), ((x1 + x2) // 2, y1)]
                        if fill:
                            pygame.draw.polygon(canvas, color, points)
                        else:
                            pygame.draw.polygon(canvas, color, points, radius)
                    elif mode == EQUILATERAL:
                        height = (3**0.5 / 2) * width
                        points = [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)]
                        if fill:
                            pygame.draw.polygon(canvas, color, points)
                        else:
                            pygame.draw.polygon(canvas, color, points, radius)
                    elif mode == RHOMBUS:
                        dx = width // 2
                        dy = height // 2
                        points = [(x1, y1 + dy), (x1 + dx, y1), (x1 + 2*dx, y1 + dy), (x1 + dx, y1 + 2*dy)]
                        if fill:
                            pygame.draw.polygon(canvas, color, points)
                        else:
                            pygame.draw.polygon(canvas, color, points, radius)
                    elif mode == LINE:
                        pygame.draw.line(canvas, color, start_pos, end_pos, radius)
                
                drawing = False  # Завершаем процесс рисования

            # Обработка движения мыши с зажатой кнопкой
            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == BRUSH:
                    # Рисование кистью - линия от предыдущей позиции к текущей
                    pygame.draw.line(canvas, color, start_pos, event.pos, radius)
                    start_pos = event.pos
                elif mode == ERASER:
                    # Стирание - рисование белых линий
                    pygame.draw.line(canvas, WHITE, start_pos, event.pos, radius)
                    start_pos = event.pos

        # Обновление экрана
        pygame.display.flip()
        # Ограничение FPS до 60 кадров в секунду
        clock.tick(60)

    # Завершение работы Pygame
    pygame.quit()

# Запуск программы, если скрипт выполняется напрямую
if __name__ == "__main__":
    main()