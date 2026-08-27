# «Спробуй виконати цей код. Якщо виникне певна помилка — не заверши всю програму, а виконай інший код».

# print("--------try_except--------")

# try:
#     number = int(input("Введи число: "))
# except ValueError:
#     print("Потрібно ввести число!")

# ValueError — це тип помилки, який виникає, коли значення має неправильний формат для певної операції.

# print("--------try_except in while--------")

# while True:
#     try:
#         points = int(input("Введи бали: "))
#         break
#     except ValueError:
#         print("Введи саме число!")

print("--------try_except with else and finally--------")

try:
    number = int("apple")
    print("A")
except ValueError:
    print("B")
else:
    print("C")
finally:
    print("D")

print("E")

# else у try: якщо помилки не виникло.
# finally виконується незалежно від того, була помилка чи ні.