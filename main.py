print("========WORD QUEST 2.0========")

words = ["apple", "dog", "sun"]
translations = ["яблуко", "собака", "сонце"]

score = 0
round_number = 0

while round_number < 3:
    print("Переклади слово:", words[round_number])

    answer = input("Твоя відповідь: ")

    if answer == translations[round_number]:
        score = score + 10
        print("Правильно!")
    else:
        print("Неправильно!")

    round_number = round_number + 1

print("Фінальний рахунок:")
print(score)