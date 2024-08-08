import random
from math import gcd
from brain_games.cli import welcome_user


def main():
    username = welcome_user()
    score = 0
    while True:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        print(f"Question: {first_number} {second_number}")
        user_answer = input("Your answer: ")
        correct_answer = gcd(first_number, second_number)
        if user_answer == str(correct_answer):
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            break

        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == "__main__":
    main()
