import prompt


rounds_to_win = 3


def lets_play(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")

    print(f"{game.task}")

    correct_answers_counter = 0
    while correct_answers_counter < rounds_to_win:
        expression, correct_answer = game.game_options()
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_counter += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user_name}!")
            return
    print('')
    print(f'Congratulatios, {user_name}!')
