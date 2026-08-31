words = ["apple", "dog", "sun"]
translations = ["яблуко", "собака", "сонце"]

score = 0
round_number = 0

# print("--------Word Quest--------")

#  for word in words:
#     print("Переклади слово:", word)

#     answer = input("Твоя відповідь: ")

#     if answer == translations[round_number]:
#         score = score + 10
#         print("Правильно!")
#     else:
#         print("Неправильно!")

#     print(score)

#     round_number = round_number + 1

# print("Фінальний рахунок:")
# print(score)

print("--------for in for--------")

for word in words:
    for letter in word:
        print(letter)

print("--------for with zip--------")

players = ["Anna", "Max", "Tom"]
levels = [2, 1, 3]

# Розпаковуємо пару (гравець, рівень) прямо в циклі:
for player, level in zip(players, levels):
    print(f"Гравець {player} має рівень {level}")

print("--------for with list in dict in dict--------")

players_data = {
    "Anna": {
        "score": 150,
        "words_learned": ["apple", "cat", "dog"]
    },
    "Max": {
        "score": 90,
        "words_learned": ["sun", "car"]
    }
}

for name, info in players_data.items():
    # info — це словник {"score": ..., "words_learned": [...]}
    words_count = len(info["words_learned"])
    print(f"{name} вивчив(ла) слів: {words_count}")