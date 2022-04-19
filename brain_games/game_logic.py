"""Brain-game logic."""


from brain_games import err_exit, greet

ROUNDS = 3


def run_logic(game):
    """Run game logic."""
    username = greet.greeting()
    rules = game.RULES
    print(rules)
    index = 0
    while index < ROUNDS:
        cond, answer = game.run_game()
        if cond == answer:
            print('Correct!')
            index += 1
        else:
            err_exit.error(cond, answer, username)
    else:
        print('Congratulations, {0}!'.format(username))
