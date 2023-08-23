from random import randint


task = 'What number is missing in the progression?'


def game_options():
    progression_step = randint(2, 10)
    progression_start = randint(1, 100)
    progression_length = 10
    progression_counter = 0
    num_list = []

    while progression_counter < progression_length:
        num_list.append(str(progression_start + progression_step * progression_counter))
        progression_counter += 1
    changing_index = randint(1, progression_length - 1)
    correct_answer = num_list[changing_index]
    num_list[changing_index] = '..'
    progression_row = ' '.join(num_list)
    return progression_row, correct_answer
