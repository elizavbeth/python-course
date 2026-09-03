print("--------Поєднуємо .split() з розпакуванням змінних--------")

line = "house:будинок"

# Одразу створюємо дві змінні:
word, translation = line.split(":")

print(f"Слово: {word}")          # Слово: house
print(f"Переклад: {translation}") # Переклад: будинок

print("--------Нюанс .split()--------")
# Важливий нюанс: Пробіли навколо роздільника!
# Якщо у твоєму файлі чи тексті є пробіли поруч із роздільником, .split() збереже їх у шматочках:

line = "apple : яблуко"

word, translation = line.split(":")

print(word)        # 'apple ' (з пробілом на кінці!)
print(translation) # ' яблуко' (з пробілом на початку!)

print("--------Виправлення нюансу .split()--------")

line = "apple : яблуко"

# Прибираємо пробіли для кожного шматочка:
word, translation = [item.strip() for item in line.split(":")]

print(word)        # 'apple'
print(translation) # 'яблуко'

print("--------Обмеження кількості розрізів: maxsplit--------")
# Іноді рядок містить багато роздільників, але нам треба розрізати його лише кілька разів.
# Наприклад, у нас є лог гри: час : гравець : дія

log = "12:00 : Max : answered correctly to cat"

# Розрізаємо тільки 2 рази:
parts = log.split(" : ", maxsplit=2)

print(parts)
# Результат: ['12:00', 'Max', 'answered correctly to cat']