"""GCD game."""

import random

import prompt

left_limit = -25
right_limit = 25
rules = 'Find the greatest common divisor of given numbers.'


def run_game():  # noqa: WPS231
    """Return variables for game logic."""
    counter = 0
    counter2 = 0
    number1 = 1
    number2 = 1
    while counter == 0:
        while number1 != 0 and number2 != 0 and counter2 == 0:
            number1 = random.randint(left_limit, right_limit)
            number2 = random.randint(left_limit, right_limit)
            counter2 += 1
        index = 1
        divisor_list = []
        while index <= min(abs(number1), abs(number2)):
            if number1 % index == 0 and number2 % index == 0:
                divisor_list.append(index)
                counter = index
            index += 1
    cond = str(max(divisor_list))
    print('Question: {0} {1}'.format(number1, number2))
    answer = prompt.string('Your answer: ')
    return (cond, answer)


if __name__ == '__main__':
    run_game()
