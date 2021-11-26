import board
import numpy as np
import random_int

class Solver():
    def __init__(self):
        self._random_generator = random_int.RandomInt()

    def solve(self):
        while True:
            _board = board.Board()
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













