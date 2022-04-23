#!/usr/bin/env python

"""Calc game launch."""

from brain_games import game_engine
from brain_games.games import calc


def main():
    """Play calculator game."""
    game_engine.run(calc)


if __name__ == '__main__':
    main()
