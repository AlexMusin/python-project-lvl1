#!/usr/bin/env python
"""GCD game launch."""

from brain_games import game_logic


def main():
    """Play gcd game."""
    game_name = 'gcd'
    game_logic.logic(game_name)


if __name__ == '__main__':
    main()
