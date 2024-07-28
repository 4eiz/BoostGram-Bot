import aiosqlite






# Добавление новой записи в таблицу requests
async def add_request(order_id, price, user_id, status):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        insert_query = '''
        INSERT INTO requests (id, price, user_id, status)
        VALUES (?, ?, ?, ?)
        '''
        await db.execute(insert_query, (order_id, price, user_id, status))
        await db.commit()
        print("Заявка успешно добавлена.")
    except aiosqlite.Error as error:
        print("Не удалось добавить новую запись в таблицу requests.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Удаление записи по ID из таблицы requests
async def delete_request(request_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        delete_query = '''
        DELETE FROM requests
        WHERE id = ?
        '''
        await db.execute(delete_query, (request_id,))
        await db.commit()
        print(f"Заявка с ID {request_id} успешно удалена.")
    except aiosqlite.Error as error:
        print("Не удалось удалить запись из таблицы requests.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Изменение статуса выполнения заявки
async def update_request_status(request_id, status):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        update_query = '''
        UPDATE requests
        SET status = ?
        WHERE id = ?
        '''
        await db.execute(update_query, (status, request_id))
        await db.commit()
        print(f"Статус заявки с ID {request_id} успешно обновлен.")
    except aiosqlite.Error as error:
        print("Не удалось обновить статус заявки.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)