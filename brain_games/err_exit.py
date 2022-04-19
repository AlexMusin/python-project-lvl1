"""Error and exit module."""
import sys


def error(cond, answer, username):
    """Say error and exit."""
    print("'{0}' is wrong answer ;(. Correct answer was '{1}.'".format(answer, cond))  # noqa: E501
    incorrect = "Let's try again, {0}!".format(username)
    print(incorrect)
    sys.exit(0)


if __name__ == '__main__':
    error()
