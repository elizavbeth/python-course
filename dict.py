# .keys()   → ключі
# .values() → значення
# .items()  → ключ + значення

words = {
    "apple": "яблуко",
    "dog": "собака",
    "sun": "сонце"
}

print("--------print() with for and .items()--------")

for word, translation in words.items():
    print("Переклади слово:", word)
    print("Правильний переклад:", translation)

print("--------print() with for--------")

for word in words:
    translation = words[word]

    print(word)
    print(translation)

print("--------print() and input() with for and .items()--------")

for word, translation in words.items():
    print("Переклади слово:", word)

    answer = input("Твоя відповідь: ")

    if answer == translation:
        print("Правильно!")
    else:
        print("Неправильно!")

print("--------Word Quest--------")

# def calculate_points(answer, correct_answer, points=10):
#     if answer == correct_answer:
#         return points
#     else:
#         return 0

words = {
    "apple": "яблуко",
    "dog": "собака",
    "sun": "сонце"
}

score = 0

for word, translation in words.items():
    print("Переклади слово:", word)

    answer = input("Твоя відповідь: ")

    if answer == translation:
        print("Правильно!")
        score += 10
    else:
        print("Неправильно!")

    print("Всього отримано балів:", score)