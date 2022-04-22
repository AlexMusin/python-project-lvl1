"""Calculator game."""

import random

import numexpr

LEFT_LIMIT = -10
RIGHT_LIMIT = 10
ACTION_LIST = ('*', '+', '-')
RULES = 'What is the result of the expression?'


def run_game():
    """Return variables for game logic."""
    number1 = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    number2 = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    action = random.choice(ACTION_LIST)
    question = '{0} {2} {1}'.format(number1, number2, action)
    condition = str(numexpr.evaluate(question))
    return (question, condition)


if __name__ == '__main__':
    run_game()
