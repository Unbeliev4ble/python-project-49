from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_options():
    number = randint(1, 100)
    correct_answer = 'yes'
    if number % 2 != 0:
        correct_answer = 'no'
    return number, correct_answer
