"""Brain-game logic."""


from brain_games import err_exit, greet


def logic(game_name):
    """Run game logic."""  # noqa: DAR101
    username = greet.greeting()
    exec('from brain_games.games import game_{0}'.format(game_name))
    rules = eval('game_{0}.RULES'.format(game_name))
    print(rules)
    index = 0
    while index < 3:
        cond, answer = eval('game_{0}.run_game()'.format(game_name))
        if cond == answer:
            print('Correct!')
            index += 1
        else:
            err_exit.error(cond, answer, username)
        if index == 3:
            print('Congratulations, {0}!'.format(username))
