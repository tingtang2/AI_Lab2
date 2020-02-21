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

testBoard = [
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','_','k', 'b', '_'],
        ['_','_','_','_','_','_', '_', 'B'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','_','_', '_', '_'],
        ['_','_','_','_','b','_', 'b', 'P'],
        ['_','_','_','p','_','P', 'P', '_'],
        ['_','_','R','_','R','_', 'K', '_']]

# Make an intial board by choosing one of the three board in main.py
board = main.Board(board1)

#board.print()

#board.getNextBoards()

test = main.Board(testBoard)


#for board in test.getNextBoards():
#    board.print()

#print(test.isCheck("white"))

#print("optimal value", main.H_Minimax(board)[0], main.H_Minimax(board)[1])

#for piece in board.getPieces():
    #piece.print()

#print(main.pieceActions('q', ('d', '4')))
'''
            toBreak = False
            for i in range(coord[1] - 1, -1, -1):
                for j in range(coord[0] + 1, DIMENSION):
                    square = (chr(i + 97), str(8 - j))
                    if board.getPieceOnSquare(square) == None:
                        squares.append(square)
                    elif self.getColor() == board.getPieceOnSquare(square).getColor():
                        toBreak = True
                        break
                    else:
                        squares.append(square)
                        toBreak = True
                        break
                if toBreak:
                    break
            print("2")
            squares.append("done2")
            toBreak = False
            for i in range(coord[1] + 1, DIMENSION):
                for j in range(coord[0] - 1, -1, -1):
                    square = (chr(i + 97), str(8 - j))
                    if board.getPieceOnSquare(square) == None:
                        squares.append(square)
                    elif self.getColor() == board.getPieceOnSquare(square).getColor():
                        toBreak = True
                        break
                    else:
                        squares.append(square)
                        toBreak = True
                        break
                if toBreak:
                    break


            print("3")
            squares.append("done3")
            toBreak = False
            for i in range(coord[1] + 1, DIMENSION):
                for j in range(coord[0] + 1, DIMENSION):
                    square = (chr(i + 97), str(8 - j))
                    if board.getPieceOnSquare(square) == None:
                        squares.append(square)
                    elif self.getColor() == board.getPieceOnSquare(square).getColor():
                        toBreak = True
                        break
                    else:
                        squares.append(square)
                        toBreak = True
                        break
                if toBreak:
                    break
            print("4")
            squares.append("done4")
            '''
>>>>>>> Stashed changes
