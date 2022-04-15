"""Greeting module."""
import prompt


def greeting():
    """Greet the Player."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    greet = ('Hello, {0}!'.format(username))
    print(greet)
    return (username)


if __name__ == '__main__':
    greeting()
