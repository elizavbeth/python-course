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


print("--------enumerate()--------")

words = ["apple", "dog", "sun"]

for index, word in enumerate(words):
    print(index, word)


print("--------.sort()--------")
# Метод .sort() змінює список і сортує його.
# Тобто за замовчуванням — від меншого до більшого.
# .sort() змінює сам список:
scores = [30, 10, 20]
scores.sort()
# Тепер:
# scores → [10, 20, 30]

print("--------sorted()--------")
# Створює новий відсортований результат:
scores = [30, 10, 20]

result = sorted(scores)
# Тепер:
# scores → [30, 10, 20]
# result → [10, 20, 30]

print("--------sorted() with key--------")
# sorted() може отримати key — тобто правило, за яким сортувати.
# Наприклад:
words = ["sun", "apple", "dog"]

result = sorted(words, key=len)
# Тут len каже: сортуй слова за їхньою довжиною.
# Отримаємо:
# ["dog", "sun", "apple"]

print("--------sum(), min(), max()--------")

scores_list = [10, 50, 20, 90, 40]

total = sum(scores_list)  # Сума всіх елементів: 210
lowest = min(scores_list)  # Найменше значення: 10
highest = max(scores_list) # Найбільше значення: 90

print(total)
print(lowest)
print(highest)


print("--------list comprehensions with numbers--------")

row_scores = [10, 0, 25, 0, 50, 5]

doubled_scores = [score * 2 for score in row_scores]
print(doubled_scores)

positive_scores = [score for score in row_scores if score > 0]
print(positive_scores)

print("--------list comprehensions with words--------")

words = ["apple", "cat", "elephant"]

word_lengths = [len(word) for word in words]
print(word_lengths)