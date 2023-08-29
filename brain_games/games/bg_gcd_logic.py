from random import randint


task = "Find the greatest common divisor of given numbers."


def find_greatest_common_divisor(num_1, num_2):
    max_num = max(num_1, num_2)
    min_num = min(num_1, num_2)
    for i in range(max_num, 0, -1):
        if max_num % i == 0 and min_num % i == 0:
            return i


def game_options():
    num_1 = randint(1, 50)
    num_2 = randint(1, 20)
    correct_answer = find_greatest_common_divisor(num_1, num_2)
    numbers = f'{num_1} {num_2}'
    return numbers, str(correct_answer)
