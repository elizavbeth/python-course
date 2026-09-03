print("========WORD QUEST 2.0========")

words = ["apple", "dog", "sun", "book", "water"]
translations = ["яблуко", "собака", "сонце", "книга", "вода"]

score = 0
round_number = 0

while round_number < len(words):
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