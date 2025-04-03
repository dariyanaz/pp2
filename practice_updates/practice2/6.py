import pygame

# Инициализация Pygame и звукового модуля
pygame.init()
pygame.mixer.init()

# Загрузка звука
sound = pygame.mixer.Sound('sound.wav')

# Воспроизведение звука
sound.play()

# Задержка, чтобы звук успел проиграться (иначе программа закроется сразу)
pygame.time.delay(3000)  # 3000 миллисекунд = 3 секунды

# Завершение работы
pygame.quit()