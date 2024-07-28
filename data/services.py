import aiosqlite
import asyncio


# Добавление новой записи в таблицу services
async def add_service(service_id, name, price):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        insert_query = '''
        INSERT INTO services (service_id, name, price)
        VALUES (?, ?, ?)
        '''
        await db.execute(insert_query, (service_id, name, price))
        await db.commit()
        print("Сервис успешно добавлен.")
    except aiosqlite.Error as error:
        print("Не удалось добавить новую запись в таблицу services.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



#Удаление записи по service_id из таблицы services
async def delete_service(service_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        delete_query = '''
        DELETE FROM services
        WHERE service_id = ?
        '''
        await db.execute(delete_query, (service_id,))
        await db.commit()
        print(f"Сервис с service_id {service_id} успешно удален.")
    except aiosqlite.Error as error:
        print("Не удалось удалить запись из таблицы services.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Получение информации о сервисе по service_id
async def get_service_info(service_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        select_query = '''
        SELECT * FROM services WHERE service_id = ?
        '''
        async with db.execute(select_query, (service_id,)) as cursor:
            service_info = await cursor.fetchone()
            if service_info:
                return service_info
            else:
                return None
    except aiosqlite.Error as error:
        print("Не удалось получить информацию о сервисе.", error)
        return None
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Обновление информации о сервисе по service_id
async def update_name(service_id, new_name):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        update_query = '''
        UPDATE services
        SET name = ?
        WHERE service_id = ?
        '''
        await db.execute(update_query, (new_name, service_id))
        await db.commit()
        print(f"Информация о сервисе с service_id {service_id} успешно обновлена.")
    except aiosqlite.Error as error:
        print("Не удалось обновить информацию о сервисе.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Обновление цены о сервисе по service_id
async def update_price(service_id, price):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        update_query = '''
        UPDATE services
        SET price = ?
        WHERE service_id = ?
        '''
        await db.execute(update_query, (price, service_id))
        await db.commit()
        print(f"Информация о сервисе с service_id {service_id} успешно обновлена.")
    except aiosqlite.Error as error:
        print("Не удалось обновить информацию о сервисе.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Функция для получения и форматирования всех записей из таблицы services
async def get_all_services():
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        select_query = '''
        SELECT id, service_id, name, price
        FROM services
        '''
        async with db.execute(select_query) as cursor:
            rows = await cursor.fetchall()
            formatted_text = ""
            for row in rows:
                formatted_text += f"Service ID: <code>{row[1]}</code>\n"
                formatted_text += f"Текст: <b>{row[2]}</b>\n"
                formatted_text += f"Цена: <code>{row[3]}</code>\n\n"
            return formatted_text
    except aiosqlite.Error as error:
        print("Не удалось получить информацию о сервисах.", error)
        return ""
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)







# service_id = 88
# name = 'RU Premium BOT START | 15-30 DAYS NO DROP'
# price = 0.07

# asyncio.run(add_service(service_id=service_id, name=name, price=price))