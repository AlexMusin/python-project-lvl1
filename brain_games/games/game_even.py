"""Odd-or-even game."""


import random

import prompt

rules = 'Answer "yes" if the number is even, otherwise answer "no".'
right_limit = -256
left_limit = 255


def run_game():
    """Return even-game variables."""
    number = random.randint(right_limit, left_limit)
    cond = number % 2 == 1
    if cond == 0:
        cond = 'yes'
    elif cond == 1:
        cond = 'no'
    print('Question: {0}'.format(number))
    answer = prompt.string('Your answer: ')
    return (cond, answer)


if __name__ == '__main__':
    run_game()
