# if умова_1:
#     # код
# elif умова_2:
#     # код
# elif умова_3:
#     # код
# else:
#     # код

print("========WORD QUEST========")

score = 0

print("Слово 1 із 3")
answer = input("Переклади слово 'apple': ")

if answer == "яблуко":
    score = score + 10
    print("Правильно!")
else:
    print("Неправильно!")

print("Поточний рахунок:")
print(score)
print("Наступне слово")

print("Слово 2 із 3")
answer = input("Переклади слово 'dog': ")

if answer == "собака":
    score = score + 10
    print("Правильно!")
else:
    print("Неправильно!")

print("Поточний рахунок:")
print(score)
print("Наступне слово")

print("Слово 3 із 3")
answer = input("Переклади слово 'sun': ")

if answer == "сонце":
    score = score + 10
    print("Правильно!")
else:
    print("Неправильно!")

print("Фінальний рахунок: ")
print(score)

if score >= 30:
    print("🏆 Ідеально!")
elif score >= 20:
    print("Добре!")
elif score >= 10:
    print("Непогано!")
else:
    print("Потрібно потренуватися!")

print("--------elif--------")

score = int(input("Введи рекорд: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

print("--------if in if--------")

score = int(input("Введи рекорд: "))
correct_answers = int(input("Введи число правильних відповідей: "))

if score >= 80:
    if correct_answers >= 8:
        print("Майстер слів!")
    else:
        print("Недостатньо правильних відповідей")

print("--------if in one line--------")

score = 80
# тернарний умовний вираз
print("Результат:", "Склав" if score >= 60 else "Не склав")
# Структура:
# значення_якщо_True if умова else значення_якщо_False