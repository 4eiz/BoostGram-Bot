## Описание проекта

Этот проект представляет собой многоюзерный Telegram-бот, который позволяет пользователям пополнять свой баланс и использовать его для накрутки статистики в Telegram (подписчики, просмотры, лайки и т.д.). 

### Основные функции:

- **Пополнение баланса:** Пользователи могут пополнять свой баланс через оплату счета в CRYPTOBOT.
- **Накрутка статистики:** Бот использует API системы сервиса [teateagram.com](https://teateagram.com) для накрутки статистики.

### Принцип работы:

1. **Пополнение счета:** Пользователь оплачивает счет через CRYPTOBOT, тем самым пополняя свой баланс в боте.
2. **Использование баланса:** Пользователь может использовать свой баланс для заказа различных услуг по накрутке статистики в Telegram.
3. **Выполнение заказов:** Бот отправляет запросы на сервис teateagram.com через их API для выполнения заказов пользователя.

## Установка и настройка

### 1. Установка зависимостей

Для начала установите все необходимые зависимости, выполнив команду:

```sh
pip install -r req.txt
```

### 2. Настройка конфигурационного файла

В конфигурационном файле необходимо указать следующие переменные:

- **BOT_TOKEN** - токен вашего Telegram-бота.
- **CRYPTO_TOKEN** - токен платёжного приложения в криптоботе.
- **ADMIN** - ID администратора.
- **SUPPORT_URL** - ссылка на поддержку. При нажатии кнопки "🛠️ Поддержка" будет осуществлён переход по этой ссылке.
- **CHANNEL_URL** - ссылка на канал. При нажатии кнопки "📫 Канал" будет осуществлён переход по этой ссылке.
- **API_KEY** - API ключ от сервиса teateagram.com.


### 3. Команды для администратора

#### 📢 Рассылка сообщений

- **/newsletter** - отправка сообщения всем пользователям. Пример использования:

```sh
/newsletter ТЕКСТ РАССЫЛКИ
```

#### 🎟️ Купоны

- **/coupons** - вывод всех существующих купонов.
- **/add_coupon** - добавление купона. Пример использования:

```sh
/add_coupon AMOUNT _ NAME
```

где:
  - **AMOUNT** - количество денег за использование купона (цифра).
  - **_** - разделитель, обязательно с пробелами.
  - **NAME** - название купона.

- **/del_coupon** - удаление купона по ID. Пример использования:

```sh
/del_coupon ID
```

где:
  - **ID** - идентификатор купона (цифра).

#### 💼 Услуги

- **/services** - вывод всех услуг накрутки.
- **/price** - изменение цены услуги. Пример использования:

```sh
/price ID _ PRICE
```

где:
  - **ID** - идентификатор услуги (цифра).
  - **_** - разделитель, обязательно с пробелами.
  - **PRICE** - новая цена за услугу (цифра).

- **/name** - изменение имени услуги. Пример использования:

```sh
/name ID _ TEXT
```

где:
  - **ID** - идентификатор услуги (цифра).
  - **_** - разделитель, обязательно с пробелами.
  - **TEXT** - новый текст услуги (заголовок, описание и т.д.).

#### 🚫 Управление пользователями

- **/ban** - бан пользователя. Пример использования:

```sh
/ban ID
```

где:
  - **ID** - идентификатор пользователя (цифра).

- **/unban** - разбан пользователя. Пример использования:

```sh
/unban ID
```

где:
  - **ID** - идентификатор пользователя (цифра).

### 4. Изменение фотографий в меню

Чтобы изменить фотографию в меню, замените фотографию с тем же названием в папке **PHOTOS**. Файл должен иметь расширение .JPG (.JPEG не подходит).

### 5. Запуск бота

Запуск бота осуществляется после настройки конфигурационного файла и установки всех зависимостей.
Команда выполнения:

```sh
pip install -r req.txt
```

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).

---

**Разработчик:** Роберт
**Контакты:** [TELEGRAM](https://t.me/che1zi)

---

📅 Последнее обновление: Июль 2024

🌟 Если у вас есть вопросы или предложения, не стесняйтесь обращаться!