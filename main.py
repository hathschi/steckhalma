#!/usr/bin/env python3
import game

game = game.Game()

game.almost_empty_test_board()

while not game.end_game():
    game.display()
    game.ask_for_and_execute_move()




