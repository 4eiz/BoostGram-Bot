import aiosqlite







# Добавление новой записи в таблицу users
async def add_user(user_id, balance=0, total_orders=0, ban_status=False):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        insert_query = '''
        INSERT INTO users (id, balance, total_orders, ban_status)
        VALUES (?, ?, ?, ?)
        '''
        await db.execute(insert_query, (user_id, balance, total_orders, ban_status))
        await db.commit()
        print("Пользователь успешно добавлен.")
    except aiosqlite.Error as error:
        print("Не удалось добавить новую запись в таблицу.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Получение информации о пользователе по ID
async def get_user_info(user_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        select_query = '''
        SELECT * FROM users WHERE id = ?
        '''
        async with db.execute(select_query, (user_id,)) as cursor:
            user_info = await cursor.fetchone()
            if user_info:
                return user_info
            else:
                return None
    except aiosqlite.Error as error:
        print("Не удалось получить информацию о пользователе.", error)
        return False
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Удаление записи по ID
async def delete_user(user_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        delete_query = '''
        DELETE FROM users
        WHERE id = ?
        '''
        await db.execute(delete_query, (user_id,))
        await db.commit()
        print(f"Пользователь с ID {user_id} успешно удален.")
    except aiosqlite.Error as error:
        print("Не удалось удалить запись из таблицы.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Изменение баланса пользователя
async def update_balance(user_id, amount):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')

        # Получение текущего баланса пользователя
        select_query = '''
        SELECT balance FROM users WHERE id = ?
        '''
        
        async with db.execute(select_query, (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row is None:
                print(f"Пользователь с ID {user_id} не найден.")
                return False
            current_balance = row[0]

        # Проверка, достаточно ли баланса для вычитания
        if amount < 0 and current_balance < abs(amount):
            print(f"Недостаточно средств на балансе для вычитания {amount}. Текущий баланс: {current_balance}.")
            return False

        # Обновление баланса
        update_query = '''
        UPDATE users
        SET balance = balance + ?
        WHERE id = ?
        '''

        await db.execute(update_query, (amount, user_id))
        await db.commit()
        print(f"Баланс пользователя с ID {user_id} успешно обновлен.")
        return True

    except aiosqlite.Error as error:
        print("Не удалось обновить баланс пользователя.", error)
        return False
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Изменение общего количества заказов пользователя
async def update_total_orders(user_id, amount):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        update_query = '''
        UPDATE users
        SET total_orders = total_orders + ?
        WHERE id = ?
        '''
        await db.execute(update_query, (amount, user_id))
        await db.commit()
        print(f"Общее количество заказов пользователя с ID {user_id} успешно обновлено.")
    except aiosqlite.Error as error:
        print("Не удалось обновить общее количество заказов пользователя.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



#Изменение статуса бана пользователя
async def update_ban_status(user_id, ban_status):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        update_query = '''
        UPDATE users
        SET ban_status = ?
        WHERE id = ?
        '''
        await db.execute(update_query, (ban_status, user_id))
        await db.commit()
        print(f"Статус бана пользователя с ID {user_id} успешно обновлен.")
    except aiosqlite.Error as error:
        print("Не удалось обновить статус бана пользователя.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)



# Функция для активации купона пользователем и обновления его баланса
async def activate_coupon(user_id, coupon_id):
    db = None
    try:
        db = await aiosqlite.connect('data/base/base.db')
        
        # Проверка, использовал ли пользователь уже этот купон
        check_query = '''
        SELECT COUNT(*)
        FROM user_coupons
        WHERE user_id = ? AND coupon_id = ?
        '''
        async with db.execute(check_query, (user_id, coupon_id)) as cursor:
            result = await cursor.fetchone()
            if result[0] > 0:
                print("Этот купон уже был использован пользователем.")
                return 1
        
        # Получение значения купона
        get_coupon_query = '''
        SELECT money
        FROM coupons
        WHERE coupon = ?
        '''
        async with db.execute(get_coupon_query, (coupon_id,)) as cursor:
            coupon = await cursor.fetchone()
            if coupon is None:
                print("Купон не найден.")
            coupon_value = coupon[0]
            # return 2
        
        # Активация купона
        insert_query = '''
        INSERT INTO user_coupons (user_id, coupon_id)
        VALUES (?, ?)
        '''
        await db.execute(insert_query, (user_id, coupon_id))
        
        # Обновление баланса пользователя
        update_balance_query = '''
        UPDATE users
        SET balance = balance + ?
        WHERE id = ?
        '''
        await db.execute(update_balance_query, (coupon_value, user_id))
        
        await db.commit()
        print(f"Купон с id {coupon_id} успешно активирован для пользователя {user_id}. Баланс увеличен на {coupon_value}.")
        return 3
    except aiosqlite.Error as error:
        print("Не удалось активировать купон и обновить баланс.", error)
    finally:
        if db:
            try:
                await db.close()
            except aiosqlite.Error as close_error:
                print("Ошибка при закрытии соединения.", close_error)
