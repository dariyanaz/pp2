'''
def save_user_info(filename):
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"{name}, {age}")

def read_user_info(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print("Содержимое файла:", file.read())

# Тестируем программу
save_user_info("user.txt")
read_user_info("user.txt")
'''
def save_user_info(filename):
    name = input()
    age = input()
    
    with open(filename, 'w') as file:
        file.write(f'{name},{age}')
        
def read_user_info(filename):
    with open(filename, 'r') as file:
        print(file.read())
        
save_user_info('user.txt')
read_user_info('user.txt')