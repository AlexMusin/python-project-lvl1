#!/usr/bin/env python

import brain_games.cli

def say_welcome():
    return ('Welcome to the Brain Games!')


def main():
    print(say_welcome())
    brain_games.cli.welcome_user()

    
if __name__ == '__main__':
    main()