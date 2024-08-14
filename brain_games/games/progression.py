from brain_games.get_username import get_username
from brain_games.generate_random_number import generate_random_number
from brain_games.game_title import GAME_TITLES
from brain_games.write_answer_text import write_answer_text


def create_question(progression_lenght):
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


def game_process():
    score = 0
    username = get_username()
    print(GAME_TITLES['progression'])
    while True:
        correct_answer, user_answer = create_question(10)
        if write_answer_text(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break
