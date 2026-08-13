words = ["apple", "dog", "sun"]
translations = ["яблуко", "собака", "сонце"]

score = 0
round_number = 0

for word in words:
    print("Переклади слово:", word)

    answer = input("Твоя відповідь: ")

    if answer == translations[round_number]:
        score = score + 10
        print("Правильно!")
        print(score)
    else:
        print("Неправильно!")
        print(score)

    round_number = round_number + 1

print("Фінальний рахунок:")
print(score)