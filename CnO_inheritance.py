# Концепція 2: Успадкування (Inheritance)

# Уявімо, що у Word Quest є звичайні картки слів, а є бонусні картки (BonusCard), 
# які дають більше балів за правильну відповідь.

# Замість того, щоб переписувати весь код з нуля, ми можемо успадкувати BonusCard від базового класу WordCard:

# Базовий (батьківський) клас:
class WordCard:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
        self.points = 10

    def get_reward(self):
        return self.points

# Дочірній клас (вказуємо батьківський у дужках):
class BonusCard(WordCard):
    def __init__(self, word, translation, bonus_multiplier):
        # викликаємо __init__ батьківського класу WordCard:
        super().__init__(word, translation)
        self.bonus_multiplier = bonus_multiplier

    # Перевизначаємо метод get_reward (Поліморфізм!):
    def get_reward(self):
        return self.points * self.bonus_multiplier

# Функція super() посилається на батьківський клас. 
# Виклик super().__init__(word, translation) дозволяє використати вже написану логіку базового класу, 
# не дублюючи код!