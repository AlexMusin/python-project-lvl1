"""Odd-or-even game."""


import random

import prompt

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LEFT_LIMIT = -256
RIGHT_LIMIT = 255


def run_game():
    """Return even-game variables."""
    number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    condition = number % 2 == 1
    if condition == 0:
        condition = 'yes'
    elif condition == 1:
        condition = 'no'
    print('Question: {0}'.format(number))
    answer = prompt.string('Your answer: ')
    return (condition, answer)


if __name__ == '__main__':
    run_game()
