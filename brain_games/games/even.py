import random
GAME_TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_data():
    question_number = random.randint(1, 10)
    print(f"Question: {question_number}")
    user_answer = input("Your answer: ")
    if question_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, user_answer
