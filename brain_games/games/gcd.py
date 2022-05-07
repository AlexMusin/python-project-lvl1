"""GCD game."""

import random

RIGHT_LIMIT = 25
RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(number1, number2):
    """Return GCD of two input integers as a string."""
    counter = 0
    while counter == 0:
        divisor = 1
        divisor_list = []
        while divisor <= min(abs(number1), abs(number2)):
            if number1 % divisor == 0 and number2 % divisor == 0:
                divisor_list.append(divisor)
                counter = divisor
            divisor += 1
    return (str(max(divisor_list)))


def run_round():
    """Return variables for game logic."""
    number1 = random.randint(1, RIGHT_LIMIT)
    number2 = random.randint(1, RIGHT_LIMIT)
    right_answer = find_gcd(number1, number2)
    question = f'{number1} {number2}'
    return (question, right_answer)
