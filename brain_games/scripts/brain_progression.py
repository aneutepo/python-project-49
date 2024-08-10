import random
from brain_games.cli import welcome_user


def create_progression(progression_lenght):
    first_element = random.randint(1, 10)
    difference = random.randint(1, 10)
    masive_of_numbers = []
    for i in range(0, 10):
        masive_of_numbers.append(first_element)
        first_element += difference

    number_of_hide_elem = random.randint(0, len(masive_of_numbers))
    correct_answer = masive_of_numbers[number_of_hide_elem]
    masive_of_numbers[number_of_hide_elem] = '*'
    return correct_answer, masive_of_numbers


def main():
    score = 0
    username = welcome_user()
    print("What number is missing in the progression?")
    while True:
        correct_answer, progression = create_progression(10)
        print(f"Question: {progression}")
        user_answer = input("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == '__main__':
    main()
