# print("--------Модуль random (Випадковість)--------")

# import random

# words = ["apple", "house", "cat", "dog"]

# # 1. Вибрати ОДНЕ випадкове слово зі списку:
# secret_word = random.choice(words)
# print(secret_word)  # Наприклад: 'cat'

# # 2. Перемішати весь список у випадковому порядку:
# random.shuffle(words)
# print(words)  # Наприклад: ['house', 'apple', 'dog', 'cat']

# # 3. Випадкове ціле число в діапазоні від 1 до 10 включно:
# random_score = random.randint(1, 10)
# print(random_score)

# print("--------Модуль time (Замір часу)--------")
# # Функція time.time() повертає поточний час у секундах. 
# # Якщо заміряти час до початку відповіді та після, можна дізнатися швидкість гравця:

# import time

# start_time = time.time()  # Фіксуємо старт

# # Уявний процес відповіді гравця (наприклад, input):
# input("Натисни Enter, коли будеш готова...")

# end_time = time.time()    # Фіксуємо фініш

# time_taken = end_time - start_time
# print(f"Ти відповіла за {time_taken:.2f} секунд!")

print("--------Завдання--------")

import random

words_list = ["banana", "cherry", "orange"]

current_word = random.choice(words_list)
print(current_word)

random_score = random.randint(50, 100)
print(random_score)

if words_list:  # Перевіряємо, чи є взагалі слова у списку
    current_word = random.choice(words_list)
else:
    print("Список слів порожній!")