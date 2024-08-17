from math import gcd
import random
from brain_games.game_engine import game_process
GAME_TITLE = 'Find the greatest common divisor of given numbers.'


def create_question():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    print(f"Question: {first_number} {second_number}")
    user_answer = input("Your answer: ")
    correct_answer = gcd(first_number, second_number)
    return str(user_answer), str(correct_answer)


def gcd_game():
    game_process(create_question, GAME_TITLE)
