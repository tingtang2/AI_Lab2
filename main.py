### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 2 CMSC 395 Artificial Intelligence

import copy


DIMENSION = 8
MAX_DEPTH = 4

class Board:
    # Object defining a chess board and use it's properties

    def __init__(self, board, turn="white", prevBoard=None, move=None):

        self.board = board
        self.myBoard = []
        self.prevBoard = prevBoard
        self.turn = turn
        self.value = None
        self.move = move

        # Added pieces to list 
        self.pieces = []

        for i in range(DIMENSION):
            self.myBoard.append([])
            for j in range(DIMENSION):
                if board[i][j] != '_':
                    newPiece = Piece(board[i][j], ( chr(j + 97),str(8 - i) ))
                    self.pieces.append(newPiece)
                    self.myBoard[i].append(newPiece)
                else:
                    self.myBoard[i].append(None)

    def print(self):
        for row in self.board:
            print(row)
        print("\n")

    def getCoord(self, square):
        return (8 - int(square[1]), ord(square[0]) - 97)

    def getPieceOnSquare(self, square):
        return self.myBoard[self.getCoord(square)[0]][self.getCoord(square)[1]]

    def getPieces(self):
        return self.pieces

    def getValue():
        return self.value

    def setValue(val):
        self.value = val

    def getNextBoards(self):
        boards = []
        for piece in self.pieces:
            if piece.getPiece().isupper() and self.turn == "white" or \
            piece.getPiece().islower() and self.turn == "black":

                #print(piece.getPiece())

                for square in piece.getMoveSquares(self):
                    #print(square)
                    canMove = False
                    move = None
                    coords = self.getCoord(square)

                    if self.myBoard[coords[0]][coords[1]] is None:
                        canMove = True
                        print ("canMove")
                    else:
                        if self.myBoard[coords[0]][coords[1]].getPiece().islower() and self.turn == "white" or \
                                self.myBoard[coords[0]][coords[1]].getPiece().isupper() and self.turn == "black":
                            canMove = True
                            print ("canMove")

                    if canMove:
                        newBoard = copy.deepcopy(self.board)
                        newBoard[coords[0]][coords[1]] = piece.getPiece()
                        oldCoords = self.getCoord(piece.getSquare())
                        newBoard[oldCoords[0]][oldCoords[1]] = '_'
                        newMove = piece.getPiece() + " to " + square[0] + square[1]
                        
                        if self.turn == "white":
                            nextBoard = Board(newBoard, turn = "black", move = newMove)
                        else:
                            nextBoard = Board(newBoard, turn = "white", move = newMove)

                        if not nextBoard.isCheck(self.turn):
                            boards.append(nextBoard)

        return boards # is empty in checkmate situation

    def isCheck(self, turn):
        for piece in self.pieces:
            for square in piece.getMoveSquares(self):
                coords = self.getCoord(square)
                if turn == "white" != piece.getColor():
                    if self.board[coords[0]][coords[1]] == 'K':
                        return True
                elif turn == "black" != piece.getColor():
                    if self.board[coords[0]][coords[1]] == 'k':
                        return True
        return False

    def __eq__(self, board):
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.board[i][j] != board.getBoard()[i][j]:
                    return False
        return True

        
class Piece:

    def __init__(self, piece, square):
        self.piece = piece 
        self.square = square

    def getColor(self):
        if self.piece.isupper():
            return "white"
        else:
            return "black"
            
    def getPiece(self):
        return self.piece

    def getSquare(self):
        return self.square

    def print(self):
        print(self.piece, self.square)

    def getMoveSquares(self, board):
        squares = []


        if self.piece == 'P':
            if int(self.square[1]) + 1 < DIMENSION:
                squares.append((self.square[0], str(int(self.square[1]) + 1)))

        elif self.piece == 'p':
             if int(self.square[1]) - 1 > 0:
                 squares.append((self.square[0], str(int(self.square[1]) - 1)))

        elif self.piece == 'N' or self.piece == 'n':
            for i in [-1, 1]:
                if 0 <= ord(self.square[0]) + i - 97 < DIMENSION:
                    for j in [-2, 2]:
                        if 1 <= int(self.square[1]) + j <= DIMENSION:
                            squares.append(( chr(ord(self.square[0]) + i), str(int(self.square[1]) + j)))
                    
            for i in [-2, 2]:
                if 0 <= ord(self.square[0]) + i - 97 < DIMENSION:
                    for j in [-1, 1]:
                        if 1 <= int(self.square[1]) + j <= DIMENSION:
                             squares.append(( chr(ord(self.square[0]) + i),str(int(self.square[1]) + j)))

        elif self.piece == 'B' or self.piece == 'b':

            coord = board.getCoord(self.square)

            count = coord[0] - 1
            for i in range(coord[1] - 1, -1, -1):
                square = (chr(i + 97), str(8 - count))
                if count < 0:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    toBreak = True
                    break
                else:
                    squares.append(square)
                    toBreak = True
                    break
                count = count - 1

            count = coord[0] + 1
            for i in range(coord[1] - 1, -1, -1):
                square = (chr(i + 97), str(8 - count))
                if count >= DIMENSION:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break
                count = count + 1

            count = coord[0] - 1
            for i in range(coord[1] + 1, DIMENSION):
                square = (chr(i + 97), str(8 - count))
                if count < 0:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    toBreak = True
                    break
                else:
                    squares.append(square)
                    toBreak = True
                    break
                count = count - 1

            count = coord[0] + 1
            for i in range(coord[1] + 1, DIMENSION):
                square = (chr(i + 97), str(8 - count))
                if count >= DIMENSION:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break
                count = count + 1
        elif self.piece == 'R' or self.piece == 'r':
             coord = board.getCoord(self.square)

             for i in range(coord[1] - 1 , -1, -1):
                 square = (chr(i + 97), self.square[1])
                 if board.getPieceOnSquare(square) == None:
                     squares.append(square)
                 elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                 else:
                     squares.append(square)
                     break

             for i in range(coord[1] + 1, DIMENSION):
                 square = (chr(i + 97), self.square[1])
                 if board.getPieceOnSquare(square) == None:
                     squares.append(square)
                 elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                 else:
                     squares.append(square)
                     break

             for i in range(coord[0] + 1, DIMENSION):
                square = (self.square[0], str(8 - i))
                if board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break

             for i in range(coord[0] - 1, -1, -1):
                square = (self.square[0], str(8 - i))
                if board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break
                        

        elif self.piece == 'Q' or self.piece == 'q':

            # Bishop moves
            coord = board.getCoord(self.square)

            count = coord[0] - 1
            for i in range(coord[1] - 1, -1, -1):
                square = (chr(i + 97), str(8 - count))
                if count < 0:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    toBreak = True
                    break
                else:
                    squares.append(square)
                    toBreak = True
                    break
                count = count - 1

            count = coord[0] + 1
            for i in range(coord[1] - 1, -1, -1):
                square = (chr(i + 97), str(8 - count))
                if count > DIMENSION:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break
                count = count + 1

            count = coord[0] - 1
            for i in range(coord[1] + 1, DIMENSION):
                square = (chr(i + 97), str(8 - count))
                if count < 0:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    toBreak = True
                    break
                else:
                    squares.append(square)
                    toBreak = True
                    break
                count = count - 1

            count = coord[0] + 1
            for i in range(coord[1] + 1, DIMENSION):
                square = (chr(i + 97), str(8 - count))
                if count > DIMENSION:
                    break
                elif board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break
                count = count + 1

            # Rook moves
            coord = board.getCoord(self.square)

            for i in range(coord[1] - 1 , -1, -1):
             square = (chr(i + 97), self.square[1])
             if board.getPieceOnSquare(square) == None:
                 squares.append(square)
             elif self.getColor() == board.getPieceOnSquare(square).getColor():
                break
             else:
                 squares.append(square)
                 break

            for i in range(coord[1] + 1, DIMENSION):
               square = (chr(i + 97), self.square[1])
               if board.getPieceOnSquare(square) == None:
                   squares.append(square)
               elif self.getColor() == board.getPieceOnSquare(square).getColor():
                   break
               else:
                   squares.append(square)
                   break

            for i in range(coord[0] + 1, DIMENSION):
                square = (self.square[0], str(8 - i))
                if board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break

            for i in range(coord[0] - 1, -1, -1):
                square = (self.square[0], str(8 - i))
                if board.getPieceOnSquare(square) == None:
                    squares.append(square)
                elif self.getColor() == board.getPieceOnSquare(square).getColor():
                    break
                else:
                    squares.append(square)
                    break

        # king
        else:
            for i in [-1, 1]:
                if 0 <= ord(self.square[0]) - 97 + i < DIMENSION:
                    squares.append((chr(ord(self.square[0]) + i), self.square[1]))
                if 1 <= int(self.square[1]) + i <= DIMENSION:
                    squares.append((self.square[0], str( int(self.square[1]) + i)))

                for j in [-1, 1]:
                    if 0 <= ord(self.square[0]) - 97 + i < DIMENSION and 1 <= int(self.square[1]) + j <= DIMENSION:
                        squares.append((chr(ord(self.square[0]) + i), str(int(self.square[1]) + j)))

        for square in squares:
            if board.getPieceOnSquare(square) is not None:
                if self.getColor() == board.getPieceOnSquare(square).getColor():
                    squares.remove(square)

        #print(self.getPiece(), squares)
        return squares


def H_Minimax(board):
    # Set up Minimax
    v = max_value(board, float("-inf"), float("inf"), 0)

    best_action = None
    for b in board.getNextBoards():
        if b.getValue() == v:
            best_action = b.getAction()

    return v

def max_value(board, alpha, beta, depth):
    if depth == MAX_DEPTH:
        return Eval(board)

    v = float("-inf")
    for b in board.getNextBoards():
        newDepth = depth + 1
        v = max(v, min_value(b, alpha, beta, newDepth))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    
    return v

def min_value(board, alpha, beta, depth):
    if depth == MAX_DEPTH:
        return Eval(board)

    v = float("inf")
    for b in board.getNextBoards():
        newDepth = depth + 1
        v = min(v, max_value(b, alpha, beta, newDepth))
        if v <= alpha:
            return v
        beta = min(beta, v)
    
    return v

def Eval(board):
    return 0
