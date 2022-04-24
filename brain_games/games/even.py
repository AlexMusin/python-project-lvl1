"""Odd-or-even game."""


import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LEFT_LIMIT = -256
RIGHT_LIMIT = 255


def run_round():
    """Return even-game variables."""
    number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    right_answer = number % 2 == 1
    if right_answer == 0:
        right_answer = 'yes'
    elif right_answer == 1:
        right_answer = 'no'
    return (number, right_answer)


if __name__ == '__main__':
    run_round()
