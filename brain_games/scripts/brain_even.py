#!/usr/bin/env python
"""Even game launch."""

from brain_games import game_logic
from brain_games.games import game_even


def main():
    """Play odd-or-even game."""
    game_logic.run_logic(game_even)


if __name__ == '__main__':
    main()
