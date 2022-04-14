"""Progression game."""

import random

import prompt

rules = 'What is the result of the expression?'


def run_game():  # noqa: WPS210
    """Return variables for game logic."""
    progr_length = random.randint(5, 12)
    left_limit = random.randint(-25, 25)
    q_index = random.randint(0, progr_length - 1)
    step = random.randint(-10, 10)
    progression = []
    element = left_limit
    while len(progression) <= progr_length:
        progression.append(element)
        element += step
    cond = str(progression[q_index])
    progression[q_index] = '..'
    print('Question: {0}'.format(progression))
    answer = prompt.string('Your answer: ')
    return (cond, answer)


if __name__ == '__main__':
    run_game()
