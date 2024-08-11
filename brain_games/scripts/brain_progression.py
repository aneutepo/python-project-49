import random
from brain_games.cli import welcome_user


def create_progression(progression_lenght):
    first_element = random.randint(1, 10)
    difference = random.randint(1, 5)
    masive_of_numbers = []
    for i in range(0, 10):
        masive_of_numbers.append(first_element)
        first_element += difference

    number_of_hide_elem = random.randint(0, len(masive_of_numbers) - 1)
    correct_answer = masive_of_numbers[number_of_hide_elem]
    masive_of_numbers[number_of_hide_elem] = '..'
    masive_of_numbers = ' '.join(map(str, masive_of_numbers))
    print("Question:", masive_of_numbers)
    return correct_answer


def check_user_answer(correct_answer, user_answer, username):
    if user_answer == str(correct_answer):
        print("Correct!")
        return True
    else:
        print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {username}!")
        return False


def main():
    score = 0
    username = welcome_user()
    print("What number is missing in the progression?")
    while True:
        correct_answer = create_progression(10)
        user_answer = input("Your answer: ")
        if check_user_answer(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == '__main__':
    main()
