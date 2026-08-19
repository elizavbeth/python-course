def calculate_points(answer, correct_answer, points=10):
    if answer == correct_answer:
        return points
    else:
        return 0

print(calculate_points(
    answer="яблуко",
    correct_answer="яблуко",
    points=20
))