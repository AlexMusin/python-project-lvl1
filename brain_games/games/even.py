"""Odd-or-even game."""


import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LEFT_LIMIT = -256
RIGHT_LIMIT = 255


def run_round():
    """Return even-game variables."""
    number = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    right_answer = 'no' if number % 2 == 1 else 'yes'
    return (number, right_answer)
