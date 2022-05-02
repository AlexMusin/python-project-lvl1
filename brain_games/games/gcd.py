"""GCD game."""

import random

RIGHT_LIMIT = 25
RULES = 'Find the greatest common divisor of given numbers.'


def generate_input():
    """Generate two non-zero integers."""
    number1 = random.randint(1, RIGHT_LIMIT)
    number2 = random.randint(1, RIGHT_LIMIT)
    return (number1, number2)


def find_gcd(inp_tuple):
    """Find GCD."""
    counter = 0
    number1, number2 = inp_tuple
    while counter == 0:
        divisor = 1
        divisor_list = []
        while divisor <= min(abs(number1), abs(number2)):
            if number1 % divisor == 0 and number2 % divisor == 0:
                divisor_list.append(divisor)
                counter = divisor
            divisor += 1
    gcd = str(max(divisor_list))
    return ((number1, number2), gcd)


def run_round():
    """Return variables for game logic."""
    question, right_answer = find_gcd(generate_input())
    question = (' '.join(map(str, question)))
    return (question, right_answer)


if __name__ == '__main__':
    run_round()
