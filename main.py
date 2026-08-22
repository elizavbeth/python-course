words = {
    "apple": "яблуко",
    "dog": "собака",
    "sun": "сонце"
}

for word, translation in words.items():
    print("Переклади слово:", word)

    answer = input("Твоя відповідь: ")

    if answer == translation:
        print("Правильно!")
    else:
        print("Неправильно!")