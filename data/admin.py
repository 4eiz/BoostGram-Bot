import aiosqlite


# Получение списка всех ID пользователей из таблицы users
async def get_all_user_ids():
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        select_query = '''
        SELECT id FROM users
        '''
        async with db.execute(select_query) as cursor:
            user_ids = [row[0] for row in await cursor.fetchall()]
        print("Список всех ID пользователей успешно получен.")
        return user_ids
    except aiosqlite.Error as error:
        print("Не удалось получить список ID пользователей.", error)
        return []
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)