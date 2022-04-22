"""Brain-game logic."""

import prompt

ROUNDS = 3


def run(game):
    """Run game logic."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    greet = ('Hello, {0}!'.format(username))
    print(greet)
    rules = game.RULES
    print(rules)
    for index in range(0, ROUNDS):
        question, condition = game.run_game()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if condition == answer:
            print('Correct!')
            index += 1
        else:
            expr = ' is wrong answer ;(. Correct answer was '
            print("'{0}'{2}'{1}'.".format(answer, condition, expr))
            incorrect = "Let's try again, {0}!".format(username)
            print(incorrect)
            break
    else:
        print('Congratulations, {0}!'.format(username))
