def check_answer(answer, correct_answer):
    return answer == correct_answer

def calculate_points(correct, points=10):
    if correct:
        return points
    else:
        return 0

def process_answer(answer, translation):
    correct = check_answer(answer, translation)
    points = calculate_points(correct)

    return correct, points

words = {
    "apple": "яблуко",
    "dog": "собака",
    "sun": "сонце"
}

score = 0

for word, translation in words.items():
    print("Переклади слово:", word)

    answer = input("Твоя відповідь: ")

    correct, points = process_answer(answer, translation)

    if correct:
        print("Правильно!")
        score += 10
    else:
        print("Неправильно!")

    print("Всього отримано балів:", score)
