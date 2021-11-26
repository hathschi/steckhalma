import numpy as np
import re, string
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

    # def search_all_valid_moves(self):
    #     moves = 
    #     #moves up
    #     for i in range(0,7):
    #         for j in range(0,5):
    #             start = [i,j]
    #             target = [i,j+2]
    #             if self._board.is_valid_move(start,target):



