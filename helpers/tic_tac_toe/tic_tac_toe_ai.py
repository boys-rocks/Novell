import random

from helpers.tic_tac_toe import tic_tac_toe_help_functions as ttt


def ai_move(game):
    win_moves = ttt.test_if_win_is_possible(game, game.COMPUTER)
    if len(win_moves) > 0:
        return random.choice(win_moves)

    lose_moves = ttt.test_if_win_is_possible(game, game.PLAYER)
    if len(lose_moves) > 0:
        return random.choice(lose_moves)

    if game.difficulty in ["impossible", "difficult"]:
        fork_moves_computer = ttt.test_if_fork_is_possible(game, game.COMPUTER)
        if len(fork_moves_computer) > 0:
            return random.choice(fork_moves_computer)

        fork_moves_player = ttt.test_if_fork_is_possible(game, game.PLAYER)
        if len(fork_moves_player) > 0:
            if game.difficulty == "impossible" and len(fork_moves_player) > 1:
                possible_force_to_block_moves = ttt.force_player_to_block(game)
                if len(possible_force_to_block_moves) > 0:
                    return random.choice(possible_force_to_block_moves)
            return random.choice(fork_moves_player)

    if game.is_empty():
        return random.choice(ttt.corner_center_side(game))
    return random.choice(ttt.center_corner_side(game))
