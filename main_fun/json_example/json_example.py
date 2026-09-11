# Коли словники та списки слів стають великими, зберігати їх у звичайних .txt файлах стає незручно 
# (доводиться вручну розбирати рядки через .split()).

# Для цього в програмуванні використовують стандартний формат JSON (JavaScript Object Notation). 
# Він зберігає структури даних Python (словники, списки) у файлах у їхньому первозданному вигляді!

# Переваги JSON:
# Словник Python перетворюється на JSON-файл за 1 рядок.
# Завантаження з JSON-файлу назад у словник Python відбувається за 1 рядок.

import json

# Наш словник у Python:
words = {
    "apple": "яблуко",
    "house": "будинок"
}

# 1. Збереження словника у JSON-файл:
with open("json_example/dictionary_example.json", "w", encoding="utf-8") as file:
    json.dump(words, file, ensure_ascii=False, indent=4)

# 2. Завантаження JSON-файлу назад у словник Python:
with open("json_example/dictionary_example.json", "r", encoding="utf-8") as file:
    loaded_words = json.load(file)

print(loaded_words["apple"])  # Виведе: яблуко