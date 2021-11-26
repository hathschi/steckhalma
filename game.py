import numpy as np
import re
import board
import re

class Game():

    def __init__(self) -> None:
        self._board = board.Board()

    def display(self):
        self._board.display()

    def ask_for_and_execute_move(self):

        while True:
            move = input('type move: ')
            start,target,valid_input = self.parse_move(move)
            if not valid_input:
                print(move,'is not a valid input format. input your move like "d2 d4"')
                continue
            if not self._board.is_valid_move(start,target):
                print(move[0:2],'->',move[2:4],'is not a valid move. Try different coordinates.')
                continue
            break

        self._board.move(start,target)

    def parse_move(self,move):

        move=re.sub(r'[\W_]+', '', move)

        try:
            start = [ord(move[0]) - 96 - 1, int(move[1]) - 1]
            target = [ord(move[2]) - 96 - 1, int(move[3]) - 1]
        except:
            return None,None,False

        return start,target,True

    def almost_empty_test_board(self):
        self._board._board = np.zeros((7,7))

        self._board._board[3,5] = 1
        self._board._board[4,4] = 1
        self._board._board[5,4] = 1

        self._board._last_moved = None
        self._board._number_moves = 0

    def end_game(self):
        if self._board.is_won():
            self.display()
            print('')
            print('************************')
            print('Congratulation! You won!')
            print('Number of moves:',self._board._number_moves)
            print('************************')

            return True

        if not self._board.has_valid_moves():
            self.display()
            print('')
            print('************************')
            print('No more valid moves left')
            print('Tokens left:',int(np.sum(self._board._board)))
            print('************************')

            return True

        return False




