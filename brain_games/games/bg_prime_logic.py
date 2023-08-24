from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_options():
    number = randint(1, 100)
    correct_answer = 'yes'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            correct_answer = 'no'
            break
    return number, correct_answer
