import prompt


def game_process(game_module):
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}")
    print(game_module.GAME_TITLE)
    for _ in range(3):
        correct_answer, user_answer = game_module.game_data()
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"Answer '{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f'Congratulations, {username}!')
