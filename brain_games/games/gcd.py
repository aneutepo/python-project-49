from math import gcd
import random
RULES = 'Find the greatest common divisor of given numbers.'


def game_data():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    question = f"{first_number} {second_number}"
    correct_answer = gcd(first_number, second_number)
    return str(correct_answer), question
