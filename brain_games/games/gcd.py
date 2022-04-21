"""GCD game."""

import random

import prompt

LEFT_LIMIT = -25
RIGHT_LIMIT = 25
RULES = 'Find the greatest common divisor of given numbers.'


def run_game():  # noqa: WPS231
    """Return variables for game logic."""
    counter = 0
    counter2 = 0
    number1 = 1
    number2 = 1
    while counter == 0:
        while number1 != 0 and number2 != 0 and counter2 == 0:
            number1 = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
            number2 = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
            counter2 += 1
        index = 1
        divisor_list = []
        while index <= min(abs(number1), abs(number2)):
            if number1 % index == 0 and number2 % index == 0:
                divisor_list.append(index)
                counter = index
            index += 1
    condition = str(max(divisor_list))
    print('Question: {0} {1}'.format(number1, number2))
    answer = prompt.string('Your answer: ')
    return (condition, answer)


if __name__ == '__main__':
    run_game()
