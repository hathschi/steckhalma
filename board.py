import numpy as np


class Board():
    _distance_right = np.asarray([2,0])
    _distance_left = np.asarray([-2,0])
    _distance_up = np.asarray([0,2])
    _distance_down = np.asarray([0,-2])

    def __init__(self) -> None:
        self._board = np.zeros((7,7))
        #TODO improve. this is not pythonic
        for i in range(7):
            for j in range(7):
                self._board[i,j] = int(self.is_on_board([i,j]))
        
        self._board[3,3] = 0

        self._last_moved = None
        self._number_moves = 0

    def is_valid_move(self,start,target):
        start = np.asarray(start)
        target = np.asarray(target)
        distance = target - start
        
        valid_distance = (
            np.all(self._distance_right == distance)
            or np.all(self._distance_left == distance)
            or np.all(self._distance_up == distance)
            or np.all(self._distance_down == distance)
        )
        if not valid_distance:
            return False
        
        mid = ((start + target) / 2).astype(int)
        valid_start = self.is_on_board(start) and 1 == self._board[start[0],start[1]]
        valid_mid   = self.is_on_board(mid) and 1 == self._board[mid[0],mid[1]]
        valid_target = self.is_on_board(target) and 0 == self._board[target[0],target[1]]

        return valid_start and valid_mid and valid_target

    def move(self,start,target):
        start = np.asarray(start)
        target = np.asarray(target)

        assert self.is_valid_move(start,target)

        if np.any(start != self._last_moved):
            self._number_moves += 1
        
        mid = ((start + target) / 2).astype(int)
        self._board[start[0],start[1]] = 0
        self._board[mid[0],mid[1]] = 0
        self._board[target[0],target[1]] = 1

        self._last_moved = target

    def is_on_board(self,coordinate):
        if 0 > coordinate[0] or coordinate[0] >= 7:
            return False
        if 0 > coordinate[1] or coordinate[1] >= 7:
            return False
        
        if 2 <= coordinate[0] < 5:
            return True
        if 2 <= coordinate[1] < 5:
            return True
        
        return False

    def are_on_board(self,coordinates):
        #TODO improve. this is not pythonic
        return np.array([self.is_on_board(coordinate) for coordinate in coordinates])


