import psycopg2
import csv

#Функция подключения к базе
def connect():
    return  psycopg2.connect(
		dbname = 'postgres',
		user = 'postgres',
		password = '12345678',
		host = 'localhost',
		port = '5432'
	)
    
#создание таблицы
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS phonebook (
					id SERIAL PRIMARY KEY,
					name VARCHAR(100),
					phone VARCHAR(20)
				);
                ''')
    conn.commit()
    cur.close()
    conn.close()
    print('Таблица создана.')
    
#Добавление вручную
def insert_manual():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные добавлены.")
    
#Загрузка из CSV
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute('INSERT INTO phonebook (name, phone) VALUES (%s, %s);', (row['name'], row['phone']))
        conn.commit()
        print('CSV данные добавлены')
    except FileNotFoundError:
        print('Файл не найден')
    cur.close()
    conn.close()

# Обновление номера телефона по имени
def update_data_p():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя для обновления: ")
    phone = input("Введите новый номер телефона: ")
    cur.execute('UPDATE phonebook SET phone = %s WHERE name = %s;', (phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные обновлены.")
    
# Обновление имени по имени
def update_data_n():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя для обновления: ")
    newname = input("Введите новое имя: ")
    cur.execute('UPDATE phonebook SET name = %s WHERE name = %s;', (newname, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные обновлены.")

# Поиск пользователя по имени
def search_user():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя для поиска: ")
    cur.execute('SELECT * FROM phonebook WHERE name = %s;', (name,))
    results = cur.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Пользователь не найден.")
    cur.close()
    conn.close()

# Удаление пользователя по имени
def delete_user():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя для удаления: ")
    cur.execute('DELETE FROM phonebook WHERE name = %s;', (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Пользователь удалён.")

# Показать всех пользователей из таблицы phonebook
def show_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Таблица пуста.")
    cur.close()
    conn.close()

def menu():
    create_table()  # создаём таблицу один раз при запуске

    while True:
        print("\n--- Меню ---")
        print("1. Добавить пользователя вручную")
        print("2. Загрузить пользователей из CSV")
        print("3. Обновить данные(номер)")
        print("4. Обновить данные(имя)")
        print("5. Поиск")
        print("6. Удаление")
        print("7. Показать всех пользователей")
        print("0. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            insert_manual()
        elif choice == '2':
            insert_from_csv('data.csv')
        elif choice == '3':
            update_data_p()
        elif choice == '4':
            update_data_n()
        elif choice == '5':
            search_user()
        elif choice == '6':
            delete_user()
        elif choice == '7':
            show_all()
        elif choice == '0':
            print("Выход.")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()