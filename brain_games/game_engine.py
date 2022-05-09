"""Brain-game engine."""

import prompt

ROUNDS = 3


def run(game):
    """Run game logic."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))
    print(game.RULES)
    for _ in range(ROUNDS):
        question, right_answer = game.run_round()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' 'is wrong answer ;(. Correct answer was' '{right_answer}'.")
            print("Let's try again, {0}!".format(username))
            break
    else:
        print('Congratulations, {0}!'.format(username))
