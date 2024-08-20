import random
GAME_TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def game_data():
    question_number = random.randint(1, 10)
    if is_prime(question_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question_number
