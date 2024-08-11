import random
from brain_games.cli import welcome_user


def get_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def check_user_answer(correct_answer, user_answer, username):
    if user_answer == correct_answer:
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
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while score < 3:
        question_number = random.randint(1, 10000)
        print(f"Question: {question_number}")
        user_answer = input("Your answer: ")
        correct_answer = get_correct_answer(question_number)
        if check_user_answer(correct_answer, user_answer, username):
            score += 1
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
