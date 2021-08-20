from helpers.tic_tac_toe import tic_tac_toe_ai


class TicTacToeGame:
    PLAYER = 1
    EMPTY = 0
    COMPUTER = -1

    def __init__(self, player_symbol, computer_symbol, starting_player, difficulty):
        self.board = {7: self.EMPTY, 8: self.EMPTY, 9: self.EMPTY,
                      4: self.EMPTY, 5: self.EMPTY, 6: self.EMPTY,
                      1: self.EMPTY, 2: self.EMPTY, 3: self.EMPTY}

        self.player_symbol = player_symbol
        self.computer_symbol = computer_symbol
        self.starting_player = starting_player
        self.difficulty = difficulty
        self.active_player = starting_player

    def make_move(self, position, specific=None):
        if specific is None:
            specific = self.active_player
        if self.board[position] != self.EMPTY:
            return False
        self.board[position] = specific
        self.active_player = self.PLAYER if self.active_player == self.COMPUTER else self.COMPUTER
        return True

    def make_ai_move(self):
        tic_tac_toe_ai.ai_move(self)

    def unmake_move(self, position):
        self.board[position] = self.EMPTY
        self.active_player = self.PLAYER if self.active_player == self.COMPUTER else self.COMPUTER

    def possible_moves(self):
        possible_moves = []
        for position, value in self.board.items():
            if value == self.EMPTY:
                possible_moves.append(position)
        return possible_moves

    def is_empty(self):
        return list(self.board.values()).count(self.EMPTY) == 9

    def check_winner(self, to_check):
        return ((self.board[7] == self.board[8] == self.board[9] == to_check) or
                (self.board[4] == self.board[5] == self.board[6] == to_check) or
                (self.board[1] == self.board[2] == self.board[3] == to_check) or
                (self.board[7] == self.board[4] == self.board[1] == to_check) or
                (self.board[8] == self.board[5] == self.board[2] == to_check) or
                (self.board[9] == self.board[6] == self.board[3] == to_check) or
                (self.board[7] == self.board[5] == self.board[3] == to_check) or
                (self.board[1] == self.board[5] == self.board[9] == to_check))

    def check_draw(self):
        return self.EMPTY not in self.board.values() and \
               not self.check_winner(self.PLAYER) and \
               not self.check_winner(self.COMPUTER)

    def check_game_over(self):
        return self.check_winner(self.PLAYER) or self.check_winner(self.COMPUTER) or self.check_draw()

    def get_winner(self):
        if self.check_winner(self.PLAYER):
            return self.PLAYER
        elif self.check_winner(self.COMPUTER):
            return self.COMPUTER
        else:
            return None

    def to_string(self, including_number_grid: bool = False):
        if including_number_grid:
            return f" {self.board[7]} | {self.board[8]} | {self.board[9]} " + " " * 10 + " 7 | 8 | 9 \n" + \
                   "---+---+---" + " " * 10 + "---+---+---" + \
                   f" {self.board[4]} | {self.board[5]} | {self.board[6]} " + " " * 10 + " 4 | 5 | 6 \n" + \
                   "---+---+---" + " " * 10 + "---+---+---" + \
                   f" {self.board[1]} | {self.board[2]} | {self.board[3]} " + " " * 10 + " 1 | 2 | 3 "
        else:
            return f" {self.board[7]} | {self.board[8]} | {self.board[9]} \n" + \
                   "---+---+---\n" + \
                   f" {self.board[4]} | {self.board[5]} | {self.board[6]} \n" + \
                   "---+---+---\n" + \
                   f" {self.board[1]} | {self.board[2]} | {self.board[3]} "
