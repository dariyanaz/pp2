'''
player_health = 3  # здоровье игрока

for enemy in enemy_cars:
    if player_rect.colliderect(enemy.rect):  # если игрок столкнулся с врагом
        player_health -= 1  # уменьшаем здоровье
        enemy_cars.remove(enemy)  # убираем машину-врага
        if player_health <= 0:
            running = False  # заканчиваем игру
'''