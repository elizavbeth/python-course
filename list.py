numbers = [1, 2, 3, 4, 5]
energy = [2, 4, 6, 8, 10]

result = [number * 2 for number in numbers] # цикл всередині списку
high_energy = [value for value in energy if value >= 8] # цикл з умовою всередині списку
result_2 = [value * 10 for value in energy if value >= 5] # цикл з умовою для перетворення чисел на відсотки

print(result)
print(high_energy)
print(result_2)

# tuple_energy = (2, 4, 6, 8, 10)
# tuple - це кортеж. Він зберігає значення, які не можна змінити.

# Множина — це структура даних, яка зберігає унікальні значення.
# "apple" in words
# Для set це особливо корисна операція — перевірка, чи є елемент у множині.


# Методи для списків:

# Метод .append() додає один елемент у кінець списку.
# words.append("sun")
# .append():
# words.append(["sun", "book"])
# додає список як один елемент:


# .extend() додає кілька елементів окремо
# words = ["apple", "dog"]
# words.extend(["sun", "book"])
# Результат: ["apple", "dog", "sun", "book"]


# .remove() видаляє перше знайдене значення зі списку.
# Наприклад:
# words = ["apple", "dog", "sun"]
# words.remove("dog")

# Якщо значення повторюється:
# words = ["apple", "dog", "apple", "sun"]
# words.remove("apple")Залишиться:
# ["dog", "apple", "sun"]
# Тобто .remove() видалив лише перший "apple".

# Важливий нюанс. Якщо значення немає:
# words.remove("cat")
# виникне помилка.


# .pop() — видалити й отримати елемент
# Наприклад:
# words = ["apple", "dog", "sun"]
# removed = words.pop(1)
# Python:
# 1. знаходить елемент з індексом 1;
# 2. це "dog";
# 3. видаляє його зі списку;
# 4. повертає "dog" у removed.
# Отримаємо:
# words   = ["apple", "sun"]
# removed = "dog"

# Можна написати:
# words.pop()
# Тоді Python видалить останній елемент.


# Метод .sort() змінює список і сортує його.
# Тобто за замовчуванням — від меншого до більшого.