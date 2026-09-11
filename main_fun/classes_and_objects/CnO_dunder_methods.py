# Концепція 3: Магічні методи (Special / Dunder Methods)
# У Python є спеціальні методи, які починаються і закінчуються двома підкресленнями __ 
# (їх називають dunder methods від double underscore).

# Головна їхня фішка: ти майже ніколи не викликаєш їх напряму. 
# Python сам автоматично викликає їх «під капотом», 
# коли ти виконуєш стандартні операції над об'єктами 
# (додавання через +, друк через print(), 
# перевірка довжини через len() або порівняння через ==).

print("--------Створення та відображення об'єкта--------")

# Створення та відображення об'єкта
# Один із них ми вже знаємо — це __init__.
# Під час створення об'єкта: card = WordCard(...)
# Конструктор. Ініціалізує початкові атрибути.

print("--------__str__(self)--------")

# __str__(self) — красиве текстове представлення об'єкта
# Коли ми робимо print(player1), 
# за замовчуванням Python виведе незрозумілий системний рядок: <__main__.Player object at 0x7f8b...>

# Якщо ж ми додамо в клас метод __str__, Python буде використовувати наш текст:

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        # Цей рядок буде виводитися при print(об'єкт)
        return f"Гравець {self.name} (Бали: {self.score})"

player1 = Player("Anna", 100)
print(player1)  # Виведе: Гравець Anna (Бали: 100)

print("--------__repr__(self)--------")

# __repr__(self) - Повертає офіційне/технічне представлення об'єкта.
# При відлагодженні, у списках [obj1, obj2]

class WordCard:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation

    def __str__(self):
        return f"Картка: {self.word} -> {self.translation}"

    def __repr__(self):
        return f"WordCard('{self.word}', '{self.translation}')"

card = WordCard("cat", "кіт")

print(card)  # Автоматично викликає __str__: "Картка: cat -> кіт"
print([card]) # У списках викликає __repr__: [WordCard('cat', 'кіт')]

print("--------Порівняння об'єктів--------")

# Порівняння об'єктів
# За замовчуванням Python порівнює об'єкти за їхньою адресою в пам'яті. 
# Але якщо ми хочемо порівнювати картки за вмістом (наприклад, чи однакові слова), 
# ми перевизначаємо магічні методи:

# __eq__(self, other)	obj1 == obj2	Дорівнює (equal)

# __lt__(self, other)	obj1 < obj2	Менше ніж (less than)

class WordCard:
    def __init__(self, word, difficulty):
        self.word = word
        self.difficulty = difficulty

    # Порівнюємо на рівність за словом:
    def __eq__(self, other):
        return self.word == other.word

    # Порівнюємо за складністю:
    def __lt__(self, other):
        return self.difficulty < other.difficulty

card1 = WordCard("apple", 1)
card2 = WordCard("apple", 3)
card3 = WordCard("boss", 5)

print(card1 == card2) # True (бо слова однакові)
print(card1 < card3)  # True (бо 1 < 5)

print("--------Математичні операції--------")

# Математичні операції
# Ти можеш навчити свої об'єкти додаватися, відніматися чи множитися!

# __add__(self, other)	obj1 + obj2

# __sub__(self, other)	obj1 - obj2

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Дозволяємо додавати бали двох гравців через +
    def __add__(self, other):
        return self.score + other.score

p1 = Player("Anna", 50)
p2 = Player("Max", 30)

total_score = p1 + p2  # Автоматично викликає p1.__add__(p2)
print(total_score)    # 80

print("--------Робота як із колекцією (контейнером)--------")

# Робота як із колекцією (контейнером)
# Якщо ти хочеш, щоб у твого об'єкта можна було виміряти довжину 
# або звертатися за індексом через квадратні дужки [ ]:

# __len__(self)	Повертає довжину	len(obj)

# __getitem__(self, index)	Дозволяє брати елемент за індексом	obj[index]

class Deck:
    def __init__(self):
        self.cards = ["apple", "house", "cat"]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

my_deck = Deck()

print(len(my_deck)) # Викличе __len__: 3
print(my_deck[0])   # Викличе __getitem__: "apple"