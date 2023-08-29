from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def game_options():
    number = randint(1, 100)
    if is_number_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
