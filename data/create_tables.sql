CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    balance REAL,
    total_orders INTEGER,
    ban_status BOOLEAN
);

CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY,
    price REAL,
    user_id INTEGER,
    status TEXT
);

CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER,
    name TEXT,
    price REAL
);

CREATE TABLE IF NOT EXISTS coupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coupon TEXT,
    money REAL
);

CREATE TABLE IF NOT EXISTS user_coupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    coupon_id INTEGER,
    used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, coupon_id)
);
