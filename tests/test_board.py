import numpy as np
import unittest

from board import Board

class TestBoard(unittest.TestCase):
    _test_board = Board()
    _test_board._board[2,3] = 0
    _test_board._board[3,5] = 0
    
    def test_are_on_board(self):
        coordinates = np.array([
            [-1,-1],
            [0,0],
            [1,1],
            [2,2],
            [3,3],
            [4,4],
            [5,5],
            [6,6],
            [7,7],
            [1,2],
            [2,1],
            [5,1],
            [1,5],
            [5,5]
        ])

        expectation = np.array([
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            False,
            False,
            True,
            True,
            False,
            False,
            False
        ])

        assert np.all(expectation == self._test_board.are_on_board(coordinates))
    
    def test_is_valid_move(self):
        moves = [
            [[0,3],[2,3]],# move right
            [[5,3],[3,3]],# move left
            [[2,1],[2,3]],# move up
            [[2,5],[2,3]],# move down
            [[1,5],[3,5]],# start off board
            [[3,0],[1,0]],# target off board
            [[3,3],[5,3]],# start empty
            [[1,3],[3,3]],# mid empty
            [[6,2],[4,2]],# target occupied
            [[4,3],[3,3]] # wrong distance
        ]

        expectations = [
            True,
            True,
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]

        for i,move in enumerate(moves):
            assert expectations[i] == self._test_board.is_valid_move(move[0],move[1])
    
    def test_invalid_move_raises_exception(self):
        with self.assertRaises(AssertionError):
            self._test_board.move([2,3], [4,3])
    
    def test_move(self):
        board = Board()
        expected_number_moves = 0

        self.assertEquals(expected_number_moves,board._number_moves)

        board.move([1,3], [3,3])
        expected_number_moves += 1

        self.assertEquals(expected_number_moves,board._number_moves)

        board.move([4,3], [2,3])
        expected_number_moves += 1

        self.assertEquals(expected_number_moves,board._number_moves)

        board.move([3,1], [3,3])
        expected_number_moves += 1

        self.assertEquals(expected_number_moves,board._number_moves)

        board.move([3,3], [1,3])
        # same token moved => expected number of moves stays the same

        self.assertEquals(expected_number_moves,board._number_moves)

    def test_are_on_board(self):
        two_dimensional_input = [
            [0,0],
            [3,3]
        ]
        
        expected_output = np.asarray([False,True])

        assert np.all(expected_output == self._test_board.are_on_board(two_dimensional_input))

        three_dimensional_input = [
            [
                [0,0],
                [3,3]
            ],
            [
                [1,1],
                [2,2],
                [6,3]
            ],
        ]
        
        expected_output = np.asarray([
            [False,True],
            [False,True,True],
        ])

        assert np.all(expected_output == self._test_board.are_on_board(three_dimensional_input))





        