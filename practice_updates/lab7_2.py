# Импорт необходимых библиотек
import pygame  # Основная библиотека для мультимедиа

# Инициализация всех модулей Pygame
pygame.init()

# Создание графического окна 
screen = pygame.display.set_mode((400, 300))
# Установка заголовка окна
pygame.display.set_caption("Music Player")

# Функция для отображения горячих клавиш в консоли
def show_hotkeys():
    print("🎵 Горячие клавиши музыкального плеера:")
    print("🔹 SPACE - Воспроизвести/Продолжить")
    print("🔹 P - Пауза")
    print("🔹 S - Остановить музыку")
    print("🔹 N - Следующий трек")
    print("🔹 B - Предыдущий трек")

# Выводим подсказки по управлению при запуске
show_hotkeys()

# Список музыкальных файлов для воспроизведения
musics = ['Нюша и Кайрат Нуртас - Алматы тундери.mp3','Naughty Boy Ft. Sam Smith - LaLaLa.mp3','Ulukmanapo - Летали.mp3','V S X V Prince - Цветы.mp3','D-Block Europe ft. Central Cee - Overseas.mp3']
# Индекс текущего трека (начинаем с первого)
track = 0
# Флаг состояния паузы (False - не на паузе, True - на паузе)
paused = False

# Загружаем первый трек для воспроизведения
pygame.mixer.music.load(musics[track])

# Функция воспроизведения/продолжения музыки
def play():
    global paused  # Используем глобальную переменную paused
    if paused:
        # Если музыка была на паузе, снимаем паузу
        pause()  # Вызываем pause() для переключения состояния
    else:
        # Если не на паузе, начинаем воспроизведение
        pygame.mixer.music.play()
        print("▶ Начало воспроизведения")

# Функция остановки музыки
def stop():
    pygame.mixer.music.stop()
    print("⏹ Воспроизведение остановлено")

# Функция паузы/продолжения
def pause():
    global paused
    if paused:
        # Если на паузе, продолжаем воспроизведение
        pygame.mixer.music.unpause()
        paused = False
        print("▶ Воспроизведение продолжено")
    else:
        # Если не на паузе, ставим на паузу
        pygame.mixer.music.pause()
        paused = True
        print("⏸ Пауза")

# Функция переключения на следующий трек
def next():
    global track, paused  # Используем глобальные переменные
    paused = False  # Снимаем паузу при переключении трека
    # Увеличиваем индекс трека с зацикливанием (% len(musics))
    track = (track + 1) % len(musics)
    # Загружаем новый трек
    pygame.mixer.music.load(musics[track])
    # Начинаем воспроизведение
    play()
    print(f"🎵 Сейчас играет: {musics[track]}")

# Функция переключения на предыдущий трек
def prev():
    global track, paused
    paused = False
    # Уменьшаем индекс трека с зацикливанием
    track = (track - 1) % len(musics)
    pygame.mixer.music.load(musics[track])
    play()
    print(f"🎵 Сейчас играет: {musics[track]}")

# Основной цикл программы
running = True
while running:
    # Заливаем экран черным цветом (RGB: 0,0,0))
    screen.fill((0, 0, 0))
    
    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Если закрыли окно, выходим из цикла
            running = False
        elif event.type == pygame.KEYDOWN:
            # Обработка нажатий клавиш
            if event.key == pygame.K_SPACE:
                play()  # Пробел - воспроизведение/продолжение
            elif event.key == pygame.K_p:
                pause()  # P - пауза/продолжение
            elif event.key == pygame.K_s:
                stop()   # S - остановка
            elif event.key == pygame.K_n:
                next()   # N - следующий трек
            elif event.key == pygame.K_b:
                prev()  # B - предыдущий трек
    
    # Отображение информации о текущем треке и статусе
    font = pygame.font.SysFont('Arial', 20)  # Шрифт для текста
    # Определяем текущий статус
    if paused:
        status = "Пауза"
    elif pygame.mixer.music.get_busy():
        status = "Воспроизведение"
    else:
        status = "Остановлено"
    # Создаем текстовую поверхность
    text = font.render(f"{musics[track]} - {status}", True, (255, 255, 255))
    # Отображаем текст в окне (координаты 20,20)
    screen.blit(text, (20, 20))
    
    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame после выхода из цикла
pygame.quit()