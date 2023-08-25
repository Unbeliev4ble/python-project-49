from random import randint


task = "Find the greatest common divisor of given numbers."


def game_options():
    num_1 = randint(1, 50)
    num_2 = randint(1, 20)
    max_num = max(num_1, num_2)
    min_num = min(num_1, num_2)
    correct_answer = 1
    numbers = f'{num_1} {num_2}'

    for i in range(max_num, 1, -1):
        if max_num % i == 0 and min_num % i == 0:
            correct_answer = i
            break
    return numbers, str(correct_answer)
