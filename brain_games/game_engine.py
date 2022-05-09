"""Brain-game engine."""

import prompt

ROUNDS = 3


def run(game):
    """Run game logic."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.RULES)
    for _ in range(ROUNDS):
        question, right_answer = game.run_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}'"
                f' is wrong answer ;(. Correct answer was '
                f"'{right_answer}'.",
            )
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
