# .keys()   → ключі
# .values() → значення
# .items()  → ключ + значення
# .get() → words.get("cat") → None

# words = {
#     "apple": "яблуко",
#     "dog": "собака",
#     "sun": "сонце"
# }

# print("--------print() with for and .items()--------")

# for word, translation in words.items():
#     print("Переклади слово:", word)
#     print("Правильний переклад:", translation)

# print("--------print() with for--------")

# for word in words:
#     translation = words[word]

#     print(word)
#     print(translation)

# print("--------print() and input() with for and .items()--------")

# for word, translation in words.items():
#     print("Переклади слово:", word)

#     answer = input("Твоя відповідь: ")

#     if answer == translation:
#         print("Правильно!")
#     else:
#         print("Неправильно!")

# print("--------Word Quest--------")

# # def calculate_points(answer, correct_answer, points=10):
# #     if answer == correct_answer:
# #         return points
# #     else:
# #         return 0

# words = {
#     "apple": "яблуко",
#     "dog": "собака",
#     "sun": "сонце"
# }

# score = 0

# for word, translation in words.items():
#     print("Переклади слово:", word)

#     answer = input("Твоя відповідь: ")

#     if answer == translation:
#         print("Правильно!")
#         score += 10
#     else:
#         print("Неправильно!")

#     print("Всього отримано балів:", score)

# print("--------dict in dict--------")

# words = {
#     "apple": {
#         "translation": "яблуко",
#         "points": 10,
#         "level": 1
#     },
#     "dog": {
#         "translation": "собака",
#         "points": 20,
#         "level": 2
#     }
# }

# print(words["apple"])

# print(words["apple"]["translation"])

# print(words["apple"]["points"])

print("--------dict in list--------")

words = [
    {
        "word": "apple",
        "translation": "яблуко",
        "points": 10
    },
    {
        "word": "dog",
        "translation": "собака",
        "points": 20
    }
]

print(words[0])

print(words[0]["word"])

print(words[1]["translation"])