# Тут ми тримаємо допоміжні функції для гри

def check_answer(user_input, correct_word):
    return user_input.strip().lower() == correct_word.strip().lower()

def calculate_bonus(time_taken):
    if time_taken < 3.0:
        return 50
    return 10