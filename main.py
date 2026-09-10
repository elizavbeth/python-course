class WordCard:
    def __init__(self, word, translation, difficulty=1):
        self.word = word
        self.translation = translation
        self.difficulty = difficulty

    def calculate_reward(self):
        return 10 * self.difficulty

hard_card = WordCard("challenge", "виклик", 3)

points = hard_card.calculate_reward()
print(points)  # Виведе: 30 (бо 10 * 3 = 30)