user_answers = ["apple", "banana", "cat", "dog"]

player_scores = [15, 0, 40, 0, 25]

is_more_than_2 = map(lambda user_answer: len(user_answer) > 2, user_answers)

print(all(is_more_than_2))

is_0 = map(lambda player_score: player_score == 0, player_scores)

print(any(is_0))

print(all([]))