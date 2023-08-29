from random import randint


task = 'What number is missing in the progression?'


def generate_progression(start, step, length):  # generate arithmetic progression
    nums_counter = 0
    progression = []
    while nums_counter < length:
        progression.append(start + step * nums_counter)
        nums_counter += 1
    return progression


def hide_random_element(row):  # convert num list into string with hidden element
    element_index = randint(1, len(row) - 1)
    hidden_element = row[element_index]
    row[element_index] = '..'
    string_row = ''
    for i in row:
        string_row += str(i) + ' '
    return string_row.strip(), hidden_element


def game_options():
    start = randint(1, 100)
    step = randint(2, 10)
    length = randint(10, 15)
    game_row = generate_progression(start, step, length)
    string_game_row, correct_answer = hide_random_element(game_row)
    return string_game_row, str(correct_answer)
