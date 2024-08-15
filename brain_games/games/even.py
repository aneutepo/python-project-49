from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES
from brain_games.game_engine import game_process


def create_question():
    question_number = generate_random_number()
    print(f"Question: {question_number}")
    user_answer = input("Your answer: ")
    if question_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, user_answer


def even_game():
    game_process(create_question, GAME_TITLES['even'])
