import random
from brain_games.get_username import get_username


def write_answer_text(correct_answer, user_answer, username):
    if user_answer == str(correct_answer):
        print("Correct!")
        return True
    else:
        print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {username}!")
        return False


def game_process():
    score = 0
    username = get_username()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while True:
        correct_answer, user_answer = create_question()
        if write_answer_text(correct_answer, user_answer, username):
            score += 1
        else:
            break
        if score == 3:
            print(f"Congratulations, {username}!")
            break


def create_question():
    question_number = random.randint(1, 10000)
    print(f"Question: {question_number}")
    user_answer = input("Your answer: ")
    correct_answer = get_correct_answer(question_number)
    return correct_answer, user_answer


def get_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    game_process()


if __name__ == "__main__":
    main()
