# Import main functionality from main
import main

board1 = [
        ['_','_','_','_','_','_', 'q', 'k'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','_','P', '_', 'p'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','_','_', 'Q', 'P'],
        ['_','_','_','_','_','P', 'P', '_'],
        ['_','_','_','_','R','_', 'K', '_']]

board2 = [
        ['_','_','B','_','_','_', '_', '_'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','K','_','_', '_', '_'],
        ['_','p','_','_','_','_', '_', '_'],
        ['_','_','k','_','_','_', '_', '_'],
        ['P','_','_','_','_','P', '_', '_'],
        ['_','B','_','_','_','_', '_', '_'],
        ['N','_','_','_','_','N', '_', '_']]

board3 = [
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','K','_','_', '_', '_'],
        ['_','_','R','_','P','_', '_', '_'],
        ['_','P','_','k','r','_', '_', '_'],
        ['_','_','_','N','p','b', '_', '_'],
        ['_','_','_','_','P','_', '_', '_'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','_','N', '_', '_']]

# Make an intial board by choosing one of the three board in main.py
board = main.Board(board1)
boardd = main.Board(board2)
boarddd = main.Board(board3)

val, move = main.H_Minimax(board)
print("optimal value board 1", val, move)
val, move = main.H_Minimax(boardd)
print("optimal value board 2", val, move)
val, move = main.H_Minimax(boarddd)
print("optimal value board 3", val, move)

