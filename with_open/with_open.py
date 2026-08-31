# with open("scores.txt", "w", encoding="utf-8") as file:
#     file.write("Anna: 100\n")

# Режим,Назва,Що робить?
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

print("--------Приклад додавання рядків:--------")

player_name = "Max"
score = 150

with open("game_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{player_name}: {score}\n")