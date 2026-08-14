print("----зрізи----")

word = "elephant"

print(word[:3])
print(word[2:5])
print(word[4:])
print(word[-3:])

print("----зрізи----")

word = "python"

print(word[:])
print(word[2:])
print(word[:-2])

print("----.lower()----")

word = "APPLE"
word = word.lower()
print(word)

print("----.lower(); .upper()----")

word = "Python"
print(word.lower())
print(word.upper())

print("----.strip()----")

answer = " яблуко "
print(answer.strip())

print("----.lower().strip()----")

correct_answer = "яблуко"
answer = input("Переклади слово 'apple': ").lower().strip()

if answer == correct_answer:
    print("Правильно!")
else:
    print("Неправильно!")

print("----.replace()----")

word = "I like cats"
word = word.replace("cats", "dogs")
print(word)

print("----.replace()----")

correct_answer = "яблуко"
answer = input("Твоя відповідь: ").strip().lower().replace("apple", "яблуко")

if answer == correct_answer:
    print("Правильно!")
else:
    print("Неправильно!")

print("----in; .find()----")

word = "elephant"
print("phant" in word)
print(word.find("phant"))
# Результат:
# True
# 3

print("----.find()----")

text = "banana"
print(text.find("a"))
# .find("a") поверне:
# 1
# Якщо .find() нічого не знайде?
# -1

print("----.find()----")

word = "banana"

first_position = word.find("a")
second_position = word.find("a", first_position + 1)

print(first_position)
print(second_position)