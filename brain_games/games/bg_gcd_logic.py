from random import randint


task = "Find the greatest common divisor of given numbers."


def game_options():
    first_num = randint(1, 50)
    second_num = randint(1, 20)
    max_num = max(first_num, second_num)
    min_num = min(first_num, second_num)
    correct_answer = 1
    numbers = f'{first_num} {second_num}'

    for i in range(max_num, 1, -1):
        if max_num % i == 0 and min_num % i == 0:
            correct_answer = i
            break
    return numbers, str(correct_answer)
