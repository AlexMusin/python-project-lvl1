#!/usr/bin/env python
"""Even game launch."""

from brain_games import game_engine
from brain_games.games import even


def main():
    """Play odd-or-even game."""
    game_engine.run(even)


if __name__ == '__main__':
    main()
