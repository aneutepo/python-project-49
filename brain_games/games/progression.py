from brain_games.game_engine import game_process
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES


def create_question():
    first_element = generate_random_number()
    difference = generate_random_number()
    masive_of_numbers = []
    for i in range(0, 10):
        masive_of_numbers.append(first_element)
        first_element += difference

    number_of_hide_elem = generate_random_number(0, len(masive_of_numbers) - 1)
    correct_answer = masive_of_numbers[number_of_hide_elem]
    masive_of_numbers[number_of_hide_elem] = '..'
    masive_of_numbers = ' '.join(map(str, masive_of_numbers))
    print("Question:", masive_of_numbers)
    user_answer = input("Your answer: ")
    return correct_answer, user_answer


def progression_game():
    game_process(create_question, GAME_TITLES['progression'])
