import prompt


def game_process(generate_question_and_answer, game_title):
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}")
    print(game_title)
    for _ in range(3):
        correct_answer, user_answer = generate_question_and_answer()
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
    print(f'Congratulations, {username}!')
