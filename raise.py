print("--------Приклад у функції перевірки для Word Quest:--------")

def set_player_age(age):
    if age < 5 or age > 100:
        # Викликаємо помилку з нашим повідомленням:
        raise ValueError("Некоректний вік гравця!")
    return age

# Обробляємо нашу викликану помилку:
try:
    user_age = int(input("Введи свій вік: "))
    set_player_age(user_age)
    print("Вік успішно збережено!")
except ValueError as e:
    print(f"Помилка: {e}")