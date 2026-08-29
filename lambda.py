print("--------lambda--------")

# lambda - це спосіб створити маленьку функцію в один рядок.

# def double(number):
#     return number * 2

double = lambda number: number * 2

print("--------lambda with map()--------")
# «Застосуй цю операцію до кожного елемента».
numbers = [1, 2, 3, 4, 5]

result = map(lambda number: number * 2, numbers)

# Але map() має одну особливість: результат map() — не список, а спеціальний об'єкт map.
# Щоб отримати список, використовують:
result = list(map(lambda number: number * 2, numbers))

print(result)

print("--------lambda with filter()--------")
# filter() дозволяє залишити тільки ті елементи, які відповідають умові.
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda number: number % 2 == 0, numbers))

print(result)


print("--------lambda with sorted()--------")

scores = {
    "Anna": 50,
    "Max": 90,
    "Tom": 70
}

result = sorted(scores.items(), key=lambda item: item[1])

print(result)
# Тут одразу кілька знайомих речей:
# items() → отримує пари ключ-значення;
# lambda → визначає, за чим сортувати;
# item[1] → бере другий елемент пари, тобто бали.
# Тому в результаті список кортежів:
# [("Anna", 50), ("Tom", 70), ("Max", 90)]

print("--------lambda with sorted(reverse=True)--------")

response_times = {
    "Player1": 4.5,
    "Player2": 2.1,
    "Player3": 3.8
}

# Сортуємо від найповільнішого до найшвидшого (4.5 -> 3.8 -> 2.1)
slowest_first = dict(sorted(response_times.items(), key=lambda item: item[1], reverse=True))

print(slowest_first)
# Результат: {'Player1': 4.5, 'Player3': 3.8, 'Player2': 2.1}