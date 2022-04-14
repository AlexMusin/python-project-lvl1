"""Calculator game."""

import random

import prompt

left_limit = -10
right_limit = 10
action_list = ('*', '+', '-')
rules = 'What is the result of the expression?'


def run_game():
    """Return variables for game logic."""
    number1 = random.randint(left_limit, right_limit)
    number2 = random.randint(left_limit, right_limit)
    action = random.choice(action_list)
    cond = str(eval('{0} {2} {1}'.format(number1, number2, action)))
    print('Question: {0} {2} {1}'.format(number1, number2, action))
    answer = prompt.string('Your answer: ')
    return (cond, answer)


if __name__ == '__main__':
    run_game()
