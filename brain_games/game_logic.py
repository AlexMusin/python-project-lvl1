"""Brain-game logic."""

import sys

import prompt

ROUNDS = 3


def greeting():
    """Greet the Player."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    greet = ('Hello, {0}!'.format(username))
    print(greet)
    return (username)


def error(cond, answer, username):
    """Say error and exit."""
    print("'{0}' is wrong answer ;(. Correct answer was '{1}.'".format(answer, cond))
    incorrect = "Let's try again, {0}!".format(username)
    print(incorrect)
    sys.exit(0)


def run_logic(game):
    """Run game logic."""
    username = greeting()
    rules = game.RULES
    print(rules)
    index = 0
    while index < ROUNDS:
        cond, answer = game.run_game()
        if cond == answer:
            print('Correct!')
            index += 1
        else:
            error(cond, answer, username)
    else:
        print('Congratulations, {0}!'.format(username))
