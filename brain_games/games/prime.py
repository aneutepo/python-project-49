import random
GAME_TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question_number):
    if question_number <= 1:
        return "no"
    elif question_number == 2:
        return "yes"
    else:
        for i in range(2, int(question_number ** 0.5) + 1):
            if question_number % i == 0:
                return "no"
        return "yes"


def game_data():
    question_number = random.randint(1, 10)
    correct_answer = is_prime(question_number)
    return correct_answer, question_number
