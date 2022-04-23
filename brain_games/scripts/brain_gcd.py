#!/usr/bin/env python
"""GCD game launch."""

from brain_games import game_engine
from brain_games.games import gcd


def main():
    """Play gcd game."""
    game_engine.run(gcd)


if __name__ == '__main__':
    main()
