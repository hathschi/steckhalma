#!/usr/bin/env python3
import game

game = game.Game()

#game._board.move([1,3],[3,3])

while True:
    game.display()
    game.ask_for_and_execute_move()



