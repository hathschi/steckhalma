import board
import numpy as np

class Solver():
    def __init__(self):
        self._board = board.Board()

    def solve(self):
        chosen_moves=[]
        while True:
            valid_moves = self._board.search_all_valid_moves()
            if not valid_moves:
                break
            chosen_move = valid_moves[np.random.randint(len(valid_moves))]
            chosen_moves += [chosen_move]
            self._board.move(chosen_move[0], chosen_move[1])
        if self._board.is_won():
            print(self._board._number_moves)
            for chosen_move in chosen_moves:
                print(chosen_move)
        else:
            self._board.display()













