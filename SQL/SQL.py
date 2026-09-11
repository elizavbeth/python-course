# SQL (Structured Query Language) — це спеціальна мова запитів, 
# за допомогою якої ми кажемо базі даних: 
# "Знайди мені користувача Anna" або "Додай 10 балів гравцю Max".

# SQLite — це найпростіша, але повноцінна база даних, яка вбудована 
# прямо в Python! Вона зберігає всі дані в одному файлі (наприклад, word_quest.db), 
# але обробляє їх за всіма правилами дорослих баз даних.

# Дані в SQL зберігаються у вигляді таблиць (як у Excel).

# Головні 4 команди SQL (CRUD):
# 1. Create (Створення) -> INSERT INTO players (name, score) VALUES ('Anna', 100)
# 2. Read (Читання) -> SELECT * FROM players WHERE score > 50
# 3. Update (Оновлення) -> UPDATE players SET score = 150 WHERE name = 'Anna'
# 4. Delete (Видалення) -> DELETE FROM players WHERE id = 1

import sqlite3

# 1. Підключаємося до файлу бази даних (якщо його немає, Python створить його сам):
connection = sqlite3.connect("SQL/word_quest.db")

# 2. Створюємо "курсор" — інструмент для виконання SQL-команд:
cursor = connection.cursor()

# 3. Створюємо таблицю гравців за допомогою SQL-запиту:
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER DEFAULT 0
)
""")

# Зберігаємо зміни та закриваємо з'єднання:
connection.commit()
connection.close()