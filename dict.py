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