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

board.print()

board.getNextBoards()

print("optimal value", board.H_Minimax(board))

#for piece in board.getPieces():
    #piece.print()

#print(main.pieceActions('q', ('d', '4')))
