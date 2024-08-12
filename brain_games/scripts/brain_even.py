import random
from brain_games.check_user_answer import check_user_answer
from brain_games.get_username import get_username


def get_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    username = get_username()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    while True:
        question_number = random.randint(1, 10000)
        print(f"Question: {question_number}")
        user_answer = input("Your answer: ")
        correct_answer = get_correct_answer(question_number)
        if check_user_answer(correct_answer, user_answer, username):
            score += 1
        else:
            break

        if score == 3:
            print(f"Congratulations, {username}!")
            break


if __name__ == "__main__":
    main()
