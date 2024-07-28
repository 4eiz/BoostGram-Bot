import aiosqlite

# Функция для добавления купона
async def add_coupon(coupon, money):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        insert_query = '''
        INSERT INTO coupons (coupon, money)
        VALUES (?, ?)
        '''
        await db.execute(insert_query, (coupon, money))
        await db.commit()
        print(f"Купон с номером {coupon} и суммой {money} успешно добавлен.")
    except aiosqlite.Error as error:
        print("Не удалось добавить купон.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Функция для удаления купона
async def delete_coupon(coupon_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        delete_query = '''
        DELETE FROM coupons
        WHERE id = ?
        '''
        await db.execute(delete_query, (coupon_id,))
        await db.commit()
        print(f"Купон с id {coupon_id} успешно удален.")
    except aiosqlite.Error as error:
        print("Не удалось удалить купон.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Функция для получения и форматирования информации о купонах
async def get_all_coupons():
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        select_query = '''
        SELECT id, coupon, money
        FROM coupons
        '''
        async with db.execute(select_query) as cursor:
            rows = await cursor.fetchall()
            formatted_text = ""
            for row in rows:
                formatted_text += f"ID: <code>{row[0]}</code>\n"
                formatted_text += f"Купон: <b>{row[1]}</b>\n"
                formatted_text += f"Сумма: <code>{row[2]}</code>\n\n"
            return formatted_text
    except aiosqlite.Error as error:
        print("Не удалось получить информацию о купонах.", error)
        return ""
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)