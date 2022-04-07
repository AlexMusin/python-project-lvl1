#!/usr/bin/env python
"""Even game launch."""

from brain_games.games import err_exit
from brain_games.games import greet
from brain_games.games import game_even


def main():
    """Play odd-or-even game."""
    username = greet.greeting()
    print(game_even.rules)
    index = 0
    while index < 3:
        condition, answer = game_even.even()
        if condition == answer:
            print('Correct!')
            index += 1
        else:
            err_exit.error()
    if index == 3:
        print('Congratulations, {0}!'.format(username))
