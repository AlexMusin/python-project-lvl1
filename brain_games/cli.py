#!/usr/bin/env python

def welcome_user():
    import prompt
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    quit()

def main():
    welcome_user()

if __name__ == '__main__':
    main()