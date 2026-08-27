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