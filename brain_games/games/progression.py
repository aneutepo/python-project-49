import random
GAME_TITLE = "What number is missing in the progression?"


def game_data():
    first_element = random.randint(1, 10)
    difference = random.randint(1, 10)
    progression_numbers = []
    for i in range(0, 10):
        progression_numbers.append(first_element)
        first_element += difference

    number_of_hide_elem = random.randint(0, len(progression_numbers) - 1)
    correct_answer = progression_numbers[number_of_hide_elem]
    progression_numbers[number_of_hide_elem] = '..'
    progression_numbers = ' '.join(map(str, progression_numbers))
    return correct_answer, progression_numbers
