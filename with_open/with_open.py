# r	Відкрити файл для читання (використовується за замовчуванням).
# w	Відкрити файл для запису. Створює новий файл, якщо він не існує, або видаляє вміст файлу, якщо існує.
# x	Відкрити файл для ексклюзивного створення. Якщо файл вже існує, операція завершується невдало.
# a	Відкрити файл для додавання даних у кінець файлу без видалення поточного вмісту. Створює новий файл, якщо він не існує.
# t	Відкрити файл в текстовому режимі (використовується за замовчуванням).
# b	Відкрити файл у двійковому режимі.
# +	Відкрити файл для оновлення (читання та запис).

# with open("scores.txt", "w", encoding="utf-8") as file:
#     file.write("Anna: 100\n")

# Режим, Назва, Що робить?
# "r" - Read (читання) - Читає файл. Якщо файлу немає — виб'є помилку FileNotFoundError.
# "w" - Write (запис) - Створює новий файл або повністю перезаписує старий (стирає все, що було!).
# "a" - Append (додавання) - Додає нові дані в кінець файлу, не видаляючи старі.

# Важливо: Параметр encoding="utf-8" ми додаємо обов'язково.
# Щоб у файлі коректно відображалися українські літери (і, є, ґ) та будь-які інші символи.

# Як читати з файлу?
# Є 3 популярні методи:
# file.read() — зчитує весь файл як один великий рядок.
# file.readline() — зчитує один рядок.
# file.readlines() або цикл for line in file: — зчитує файл по рядках (ідеально для обробки великих списків).

# print("--------Приклад читання по рядках:--------")

# with open("scores.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         clean_line = line.strip()  # .strip() прибирає символ переходу на новий рядок \n
#         print(clean_line)

# print("--------Приклад додавання рядків:--------")

# player_name = "Max"
# score = 150

# with open("game_log.txt", "a", encoding="utf-8") as file:
#     file.write(f"{player_name}: {score}\n")

# print("--------Приклад додавання рядків з dict:--------")

# new_words = {"sun": "сонце", "tree": "дерево"}

# with open("dictionary.txt", "a", encoding="utf-8") as file:
#     for word, translation in new_words.items():
#         file.write(f"{word}:{translation}\n")

print("--------Генератор Таблиці Лідерів--------")

with open("with_open/raw_log.txt", "r", encoding="utf-8") as reader, \
     open("with_open/leaderboard.txt", "w", encoding="utf-8") as writer:

    for line in reader:
        # 1. Розпаковуємо та очищаємо від пробілів і \n
        name, correct_str, questions_str, time_str = [item.strip() for item in line.split("|")]

        # 2. Перетворюємо рядки у числа
        correct = int(correct_str)
        total = int(questions_str)
        time_sec = float(time_str)

        # 3. Рахуємо точність
        accuracy = (correct / total) * 100

        # 4. Записуємо відформатований рядок у файл
        writer.write(f"{name:<10} | Точність: {accuracy:.1f}% | Час: {time_sec:.2f} сек\n")

