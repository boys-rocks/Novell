def corner_move(game):
    return list(set(game.possible_moves()) & {1, 3, 7, 9})


def center_move(game):
    return list(set(game.possible_moves()) & {5})


def side_move(game):
    return list(set(game.possible_moves()) & {2, 4, 6, 8})


def test_if_win_is_possible(game, to_check=None):
    if to_check is None:
        to_check = game.active_player
    possible_moves = []
    for move in game.possible_moves():
        game.make_move(move, to_check)
        if game.check_winner(to_check):
            possible_moves.append(move)
        game.unmake_move(move)
    return possible_moves


def test_if_fork_is_possible(game, to_check=None):
    if to_check is None:
        to_check = game.active_player
    possible_moves = []
    for move in game.possible_moves():
        game.make_move(move, to_check)
        if len(test_if_win_is_possible(game, to_check)) > 1:
            possible_moves.append(move)
        game.unmake_move(move)
    return possible_moves


def force_player_to_block(game):
    possible_moves = []
    for move in game.possible_moves():
        game.make_move(move)
        possible_win_moves = test_if_win_is_possible(game, game.COMPUTER)
        if possible_win_moves:
            game.make_move(possible_win_moves[0], game.PLAYER)
            if len(test_if_win_is_possible(game, game.PLAYER)) < 2:
                possible_moves.append(move)
            game.unmake_move(possible_win_moves[0])
        game.unmake_move(move)
    return possible_moves


# ai functions:


def corner_center_side(game):
    possible_moves = corner_move(game)
    if len(possible_moves) > 0:
        return possible_moves

    possible_moves = center_move(game)
    if len(possible_moves) > 0:
        return possible_moves

    possible_moves = side_move(game)
    if len(possible_moves) > 0:
        return possible_moves


def center_corner_side(game):
    possible_moves = center_move(game)
    if len(possible_moves) > 0:
        return possible_moves

    possible_moves = corner_move(game)
    if len(possible_moves) > 0:
        return possible_moves

    possible_moves = side_move(game)
    if len(possible_moves) > 0:
        return possible_moves
