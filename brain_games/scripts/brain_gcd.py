import random
from brain_games.get_username import get_username
from math import gcd
from brain_games.check_user_answer import check_user_answer


def create_question():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    print(f"Question: {first_number} {second_number}")
    user_answer = input("Your answer: ")
    correct_answer = gcd(first_number, second_number)
    return user_answer, correct_answer


def main():
    username = get_username()
    print("Find the greatest common divisor of given numbers.")
    score = 0
    while True:
        user_answer, correct_answer = create_question()
        if check_user_answer(correct_answer, user_answer, username):
            score += 1
        else:
            break

        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == "__main__":
    main()
