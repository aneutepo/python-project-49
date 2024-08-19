import random
GAME_TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    question_number = random.randint(1, 10)
    if question_number <= 1:
        correct_answer = "no"
    elif question_number == 2:
        correct_answer = "yes"
    else:
        correct_answer = "yes"
        for i in range(2, int(question_number ** 0.5) + 1):
            if question_number % i == 0:
                correct_answer = "no"
                break
    return correct_answer, question_number
