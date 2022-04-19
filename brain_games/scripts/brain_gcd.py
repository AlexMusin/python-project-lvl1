#!/usr/bin/env python
"""GCD game launch."""

from brain_games import game_logic
from brain_games.games import gcd


def main():
    """Play gcd game."""
    game_logic.run_logic(gcd)


if __name__ == '__main__':
    main()
