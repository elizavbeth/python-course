# Тут гра запускається

# # Щоб використати ці функції в main.py, у нас є 3 способи імпорту:

# # Спосіб 1: Імпорт всього модуля

# import helpers

# # Звертаємося через крапку: назва_модуля.назва_функції
# is_correct = helpers.check_answer("apple", "apple")

# # Спосіб 2: Точковий імпорт конкретних функцій (найпопулярніший!)

# from helpers import check_answer, calculate_bonus

# # Викликаємо напряму без префіксу helpers.:
# is_correct = check_answer("apple", "apple")
# bonus = calculate_bonus(2.5)

# # Спосіб 3: Імпорт із псевдонімом (псевдонім через as)

# import helpers as hp

# is_correct = hp.check_answer("apple", "apple")

from game_logic import format_score

result = format_score("Anna", "120")