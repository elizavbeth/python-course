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