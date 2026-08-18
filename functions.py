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