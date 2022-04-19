#!/usr/bin/env python
"""GCD game launch."""

from brain_games import game_logic
from brain_games.games import game_gcd


def main():
    """Play gcd game."""
    game_logic.logic(game_gcd)


if __name__ == '__main__':
    main()
