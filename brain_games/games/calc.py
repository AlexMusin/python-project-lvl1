"""Calculator game."""

import random

LEFT_LIMIT = -10
RIGHT_LIMIT = 10
OPERATORS_LIST = ('*', '+', '-')
RULES = 'What is the result of the expression?'


def run_round():
    """Return variables for game logic."""
    number1 = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    number2 = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
    operation = random.choice(OPERATORS_LIST)
    question = f'{number1} {operation} {number2}'
    if operation == '*':
        right_answer = number1 * number2
    elif operation == '-':
        right_answer = number1 - number2
    elif operation == '+':
        right_answer = number1 + number2
    right_answer = str(right_answer)
    return (question, right_answer)
