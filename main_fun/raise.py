# print("--------Приклад перший у функції перевірки для Word Quest:--------")

# def set_player_age(age):
#     if age < 5 or age > 100:
#         # Викликаємо помилку з нашим повідомленням:
#         raise ValueError("Некоректний вік гравця!")
#     return age

# # Обробляємо нашу викликану помилку:
# try:
#     user_age = int(input("Введи свій вік: "))
#     set_player_age(user_age)
#     print("Вік успішно збережено!")
# except ValueError as e:
#     print(f"Помилка: {e}")

# print("--------Приклад другий у функції перевірки для Word Quest:--------")

# def add_word(word, translation):
#     if len(word) == 0 or len(translation) == 0:
#         raise ValueError("Слово та переклад не можуть бути порожніми!")
#     return f"Слово {word} додано!"

# try:
#     add_word("", "кіт")
#     print("Слова успішно збережено!")
# except ValueError as e:
#     print(f"Не вдалося додати слово: {e}")

print("--------Приклад перехоплення будь-якої помилки:--------")

# Ось чому важливо перехоплювати або конкретний тип помилки, 
# або використовувати базовий клас Exception, якщо ми хочемо зловити взагалі будь-яку помилку:

try:
    raise TypeError("Помилка типу")
except Exception as e:
    print(f"Спіймано будь-яку помилку: {e}")