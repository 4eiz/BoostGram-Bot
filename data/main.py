import sqlite3

def script(name_file):
    try:
        sqlite_connection = sqlite3.connect("data/base/base.db")
        cursor = sqlite_connection.cursor()
        try:
            with open(name_file, 'r') as file:
                sql_script = file.read()
        except Exception as error:
            if sqlite_connection:
                cursor.close()
            exit(error)
        cursor.executescript(sql_script)
        sqlite_connection.commit()
        print("Скрипт выполнен успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

# script("data/create_tables.sql")