def show_rules():
    print("Правила Word Quest:")
    print("1. Переклади слово.")
    print("2. Отримай бали за правильну відповідь.")

show_rules()

print("--------параметри / аргументи--------")

def greet(name):
    print("Привіт,", name)

greet("Anna")
# Параметр — змінна, яку функція очікує отримати (name).
# Аргумент — конкретне значення, яке ми передаємо під час виклику ("Anna").

# break негайно припиняє виконання циклу.
# А continue каже: «Цю ітерацію пропусти й переходь до наступної».
# pass      → нічого
# continue  → наступна ітерація
# break     → кінець циклу
# return    → кінець функції

print("--------def + return--------")

def calculate_points(answer, correct_answer):
    if answer == correct_answer:
        return 10
    else:
        return 0
    
score = 0

answer = input("Переклади apple: ")
points = calculate_points(answer, "яблуко")
score = score + points
print(score)

answer = input("Переклади dog: ")
points = calculate_points(answer, "собака")
score = score + points
print(score)

# show_word("apple", translation="яблуко", points=20)
# Спочатку позиційні аргументи, а потім іменовані

# Можна записувати декілька позиційних аргументів у виклику за допомогою параметру *args
# Можна записувати декілька іменованих аргументів у виклику за допомогою параметру **kwargs
# *other також збирає залишок, але вже під час розпакування.

print("--------виклик у виклику--------")

def check_answer(answer, correct_answer):
    return answer == correct_answer

def show_result(correct):
    if correct:
        print("Правильно!")
    else:
        print("Неправильно!")

def calculate_points(answer, correct_answer, points=10):
    if answer == correct_answer:
        return points
    else:
        return 0

words = {
    "apple": "яблуко",
    "dog": "собака",
    "sun": "сонце"
}

score = 0

for word, translation in words.items():
    print("Переклади слово:", word)

    answer = input("Твоя відповідь: ")

    show_result(check_answer("яблуко", "яблуко"))

    points = calculate_points(answer, translation)
    score = score + points
    print("Всього отримано балів:", score)

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
# Тому результат:
# [("Anna", 50), ("Tom", 70), ("Max", 90)]