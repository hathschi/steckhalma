import board
import numpy as np
import random_int

class Solver():
    def __init__(self):
        self._random_generator = random_int.RandomInt()

    def solve(self):
        while True:
            _board = board.Board()

            _board._board = np.zeros((7,7))
            _board._board[1,2] = 1
            _board._board[1,3] = 1
            _board._board[2,4] = 1
            _board._board[5,3] = 1
            _board._board[5,4] = 1
            _board._board[6,4] = 1
            _board._last_moved = [1,2]
            _board._number_moves = 0

            chosen_moves=[]
            while True:
                valid_moves = _board.search_all_valid_moves()
                if not valid_moves:
                    break
                chosen_move = valid_moves[np.random.randint(len(valid_moves))]
                #chosen_move = valid_moves[self._random_generator.next(len(valid_moves))]
                chosen_moves += [chosen_move]
                _board.move(chosen_move[0], chosen_move[1])

            if _board.is_won():
                print(_board._number_moves)
                for chosen_move in chosen_moves:
                    print(chosen_move)
                break
            else:
                _board.display()

    def generate_target_configurations(self):
        board_hashes = []
        boards = []
        for n in range(10):
            _board = board.Board()
            _board.almost_empty()
            chosen_moves=[]
            for m in range(4):
                valid_moves = _board.search_all_valid_backward_moves()
                if not valid_moves:
                    break
                chosen_move = valid_moves[np.random.randint(len(valid_moves))]
                #chosen_move = valid_moves[self._random_generator.next(len(valid_moves))]
                chosen_moves += [chosen_move]
                _board.move_backwards(chosen_move[0], chosen_move[1])

            boards += [_board._board]
            board_hash = hash(_board.without_metadata)

            board_hashes += [board_hash]


        return np.sort(np.asarray(board_hashes))















