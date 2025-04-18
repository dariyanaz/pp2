import psycopg2
import json

def connect():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='12345678',
        host='localhost',
        port='5432'
    )

'''
1. Поиск по шаблону (функция)
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.name, phonebook.phone
    FROM phonebook
    WHERE phonebook.name ILIKE '%' || pattern || '%'
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

2. Вставка или обновление одного пользователя (процедура)
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

3. Массовое добавление пользователей из JSON (процедура)
CREATE OR REPLACE PROCEDURE insert_multiple_users(p_users JSON)
LANGUAGE plpgsql AS $$
DECLARE
    user_data JSON;
    name TEXT;
    phone TEXT;
    incorrect_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR user_data IN SELECT * FROM json_array_elements(p_users)
    LOOP
        name := user_data->>'name';
        phone := user_data->>'phone';

        IF phone ~ '^\d{10}$' THEN
            INSERT INTO phonebook(name, phone) VALUES (name, phone);
        ELSE
            incorrect_data := array_append(incorrect_data, name || ' - ' || phone);
        END IF;
    END LOOP;

    IF array_length(incorrect_data, 1) > 0 THEN
        RAISE NOTICE 'Incorrect data: %', incorrect_data;
    END IF;
END;
$$;

4. Пагинация (функция)
CREATE OR REPLACE FUNCTION get_users_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.name, phonebook.phone
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

5. Удаление по имени или номеру (процедура)
CREATE OR REPLACE PROCEDURE delete_user_by_name_or_phone(p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSE
        RAISE EXCEPTION 'You must provide either a name or a phone number';
    END IF;
END;
$$;
'''

def call_search_by_pattern():
    conn = connect()
    cur = conn.cursor()
    pattern = input("Введите шаблон для поиска: ")
    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    cur.close()
    conn.close()

def call_insert_or_update():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Пользователь добавлен или обновлён.")

def call_insert_many():
    conn = connect()
    cur = conn.cursor()
    data = []
    n = int(input("Сколько пользователей добавить? "))
    for _ in range(n):
        name = input("Имя: ")
        phone = input("Телефон (10 цифр): ")
        data.append({"name": name, "phone": phone})
    json_data = json.dumps(data)
    cur.execute("CALL insert_multiple_users(%s);", (json_data,))
    conn.commit()
    cur.close()
    conn.close()
    print("Пользователи добавлены. Проверьте PostgreSQL консоль на ошибки в номерах.")

def call_paginated():
    conn = connect()
    cur = conn.cursor()
    limit = int(input("Введите лимит: "))
    offset = int(input("Введите смещение (offset): "))
    cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    cur.close()
    conn.close()

def call_delete():
    conn = connect()
    cur = conn.cursor()
    choice = input("Удалить по (1) имени или (2) номеру телефона? ")
    if choice == '1':
        name = input("Введите имя: ")
        cur.execute("CALL delete_user_by_name_or_phone(%s, NULL);", (name,))
    elif choice == '2':
        phone = input("Введите телефон: ")
        cur.execute("CALL delete_user_by_name_or_phone(NULL, %s);", (phone,))
    else:
        print("Неверный выбор.")
        cur.close()
        conn.close()
        return
    conn.commit()
    cur.close()
    conn.close()
    print("Удаление завершено.")

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
    while True:
        print("\n--- Меню PhoneBook ---")
        print("1. Поиск по шаблону")
        print("2. Добавить/обновить пользователя")
        print("3. Массовое добавление пользователей")
        print("4. Получить с пагинацией")
        print("5. Удалить пользователя")
        print("6. Показать таблицу")
        print("0. Выход")

        choice = input("Выберите опцию: ")
        if choice == '1':
            call_search_by_pattern()
        elif choice == '2':
            call_insert_or_update()
        elif choice == '3':
            call_insert_many()
        elif choice == '4':
            call_paginated()
        elif choice == '5':
            call_delete()
        elif choice == '6':
            show_all()
        elif choice == '0':
            print("Выход.")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()

