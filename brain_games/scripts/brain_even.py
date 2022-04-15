#!/usr/bin/env python
"""Even game launch."""

from brain_games import game_logic


def main():
    """Play odd-or-even game."""
    game_name = 'even'
    game_logic.logic(game_name)


if __name__ == '__main__':
    main()
