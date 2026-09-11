import json
import random
import time

def load_words(filename):
    """Завантажуємо словник з файлу JSON з обробкою помилки."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл словника не знайдено! Використовуємо резервний словник.")
        return {"apple": "яблуко", "cat": "кіт"}

def start_game():
    # Вказуємо папку та ім'я файлу через слеш
    words_db = load_words("dictionary_game/dictionary.json")
    words_keys = list(words_db.keys())
    
    player_name = input("Введи своє ім'я: ").strip()
    score = 0
    rounds = 3
    
    print(f"\nПривіт, {player_name}! Починаємо Word Quest ({rounds} раундів).\n")
    
    start_time = time.time()
    
    for r in range(1, rounds + 1):
        target_word = random.choice(words_keys)
        correct_translation = words_db[target_word]
        
        user_input = input(f"Раунд {r}: Як перекладається '{target_word}'? ").strip().lower()
        
        if user_input == correct_translation.lower():
            score += 10
            print("✨ Правильно! (+10 балів)\n")
        else:
            print(f"❌ Невірно! Правильна відповідь: {correct_translation}\n")
            
    total_time = time.time() - start_time
    
    # Підсумок гри
    print("=" * 30)
    print(f"Гру завершено, {player_name}!")
    print(f"Твій рахунок: {score} балів")
    print(f"Загальний час: {total_time:.2f} сек")
    print("=" * 30)

if __name__ == "__main__":
    start_game()