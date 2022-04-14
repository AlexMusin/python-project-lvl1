"""Error and exit module."""
import sys


def error(cond, answer, username):
    """Say error and exit."""  # noqa: DAR101
    print("'{0}' is wrong answer ;(. Correct answer was '{1}.'".format(answer, cond))  # noqa: E501
    incorrect = "Let's try again, {0}!".format(username)
    sys.exit(incorrect)


if __name__ == '__main__':
    error()
