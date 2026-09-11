class WordCard:
    """Клас для окремого слова."""
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation

class GameEngine:
    """Клас, який керує логікою гри."""
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.cards = [
            WordCard("apple", "яблуко"),
            WordCard("house", "будинок")
        ] # У Python всі функції та методи є об'єктами першого класу (first-class citizens). 
        # Це означає, що метод можна передавати як звичайну змінну, 
        # зберігати у списках чи словниках і викликати пізніше.

    def start(self):
        print(f"Гра почалася для {self.player_name}!")
        for card in self.cards:
            user_answer = input(f"Переклад '{card.word}': ").strip()
            if user_answer.lower() == card.translation:
                self.score += 10
                print("Правильно!")
        print(f"Підсумок: {self.score} балів.")

# Запуск гри:
game = GameEngine("Anna")
game.start()