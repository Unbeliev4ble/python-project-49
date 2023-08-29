from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return number % 2 == 0


def game_options():
    number = randint(1, 100)
    if is_number_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
