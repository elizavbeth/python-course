# Концепція 3: Магічні методи (Special / Dunder Methods)
# У Python є спеціальні методи, які починаються і закінчуються двома підкресленнями __ 
# (їх називають dunder methods від double underscore).

# Один із них ми вже знаємо — це __init__. 
# Але є ще два дуже важливих методи для красивого виводу та порівняння об'єктів.

# 1. __str__(self) — красиве текстове представлення об'єкта
# Коли ми робимо print(player1), 
# за замовчуванням Python виведе незрозумілий системний рядок: <__main__.Player object at 0x7f8b...>

# Якщо ж ми додамо в клас метод __str__, Python буде використовувати наш текст:

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        # Цей рядок буде виводитися при print(об'єкт)
        return f"Гравець {self.name} (Бали: {self.score})"

player1 = Player("Anna", 100)
print(player1)  # Виведе: Гравець Anna (Бали: 100)

# 2. __len__(self) — дозволяє використовувати функцію len() на об'єкті
# Наприклад, кількість вивчених слів гравця:

class Player:
    def __init__(self, name):
        self.name = name
        self.words = ["apple", "cat", "dog"]

    def __len__(self):
        return len(self.words)

player1 = Player("Anna")
print(len(player1))  # Виведе: 3