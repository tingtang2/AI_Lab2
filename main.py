### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 2 CMSC 395 Artificial Intelligence

import copy


DIMENSION = 8

class Board:
    # Object defining a chess board and use it's properties

    def __init__(self, board, prevBoard=None):

        self.board = board
        self.prevBoard = prevBoard

        # Added pieces to dictionary
        self.pieces = []

        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.board[i][j] != '_':
                    newPiece = Piece(self.board[i][j], ( chr(j + 97),str(8 - i) ))
                    self.pieces.append(newPiece)

    def print(self):
        for row in self.board:
            print(row)

    def getPieces(self):
        return self.pieces

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

    def print(self):
        print(self.piece, self.square)

    def getMoveSquares(self, pieces):
        squares = []

        if self.piece == 'P':
            if int(square[1]) + 1 < DIMENSION:
                squares.append((square[0], str(int(self.square[1]) + 1)))

        elif self.piece == 'p':
             if int(square[1]) - 1 > 0:
                 squares.append((square[0], str(int(self.square[1]) - 1)))

        elif self.piece == 'N' or self.piece == 'n':
            for i in [-1, 1]:
                if 0 <= ord(self.square[0] + i - 97) < DIMENSION:
                    for j in [-2, 2]:
                        if 1 <= int(self.square[1]) + j <= DIMENSION:
                            squares.append(( chr(ord(self.square[0]) + i), str(int(self.square[1]) + j)))
                    
            for i in [-2, 2]:
                if 0 <= ord(square[0] + i - 97) < DIMENSION:
                    for j in [-1, 1]:
                        if 1 <= int(self.square[1]) + j <= DIMENSION:
                             squares.append(( chr(ord(square[0]) + i),str(int(self.square[1]) + j)))

        elif self.piece == 'B' or self.piece == 'b':

            count = 1
            for i in range(ord(self.square[0]) - 96, DIMENSION):
                for j in [-1, 1]:
                    if 1 <= int(self.square[1]) + j*count <= DIMENSION:
                        squares.append((chr(i + 97), str(int(self.square[1]) + j*count)))
                count = count + 1

            count = 1
            for i in range(ord(self.square[0]) - 98, -1, -1):
                for j in [-1, 1]:
                    if 1 <= int(self.square[1]) + j*count <= DIMENSION:
                        squares.append((chr(i + 97), str(int(square[1]) + j*count)))
                count = count + 1

        elif self.piece == 'R' or self.piece == 'r':
             for i in range(DIMENSION):
                 if i + 1 != int(square[1]):
                    squares.append((self.square[0], str(i + 1)))

             for i in range(DIMENSION):
                 if i != ord(square[0]) - 97:
                    squares.append((chr(i + 97), self.square[1]))

        elif self.piece == 'Q' or self.piece == 'q':

            # Bishop moves
            count = 1
            for i in range(ord(self.square[0]) - 96, DIMENSION):
                for j in [-1, 1]:
                    if 1 <= int(self.square[1]) + j*count <= DIMENSION:
                        squares.append((chr(i + 97), str(int(self.square[1]) + j*count)))
                count = count + 1

            count = 1

            for i in range(ord(self.square[0]) - 98, -1, -1):
                for j in [-1, 1]:
                    if 1 <= int(self.square[1]) + j*count <= DIMENSION:
                        squares.append((chr(i + 97), str(int(square[1]) + j*count)))
                count = count + 1

            # Rook moves
            for i in range(DIMENSION):
                 if i + 1 != int(square[1]):
                    squares.append((self.square[0], str(i + 1)))

            for i in range(DIMENSION):
                if i != ord(square[0]) - 97:
                    squares.append((chr(i + 97), self.square[1]))

        # king

        else:
            for i in [-1, 1]:
                if 0 <= ord(self.square[0]) - 97 + i < DIMENSION:
                    squares.append((chr(ord(self.square[0]) + i), self.square[1]))
                if 1 <= int(square[1]) + i <= DIMENSION:
                    squares.append((self.square[0], str( int(self.square[1]) + i)))

                for j in [-1, 1]:
                    if 0 <= ord(self.square[0]) - 97 + i < DIMENSION and 1 <= int(self.square[1]) + j <= DIMENSION:
                        squares.append((chr(ord(self.square[0]) + i), str(int(self.square[1]) + j)))

        return squares

def pieceActions(piece, square):

    # Squares piece can move to not considering enemy pieces
    squares = []

    if piece == 'P':
        if int(square[1]) + 1 < DIMENSION:
            squares.append((square[0], str(int(square[1]) + 1)))

    elif piece == 'p':
         if int(square[1]) - 1 > 0:
             squares.append((square[0], str(int(square[1]) - 1)))

    elif piece == 'N' or piece == 'n':
        for i in [-1, 1]:
            if 0 <= ord(square[0]) + i - 97 < DIMENSION:
                for j in [-2, 2]:
                    if 1 <= int(square[1]) + j <= DIMENSION:
                        squares.append(( chr(ord(square[0]) + i), str(int(square[1]) + j)))
                
        for i in [-2, 2]:
            if 0 <= ord(square[0]) + i - 97 < DIMENSION:
                for j in [-1, 1]:
                    if 1 <= int(square[1]) + j <= DIMENSION:
                         squares.append(( chr(ord(square[0]) + i),str(int(square[1]) + j)))
    
    elif piece == 'B' or piece == 'b':
        count = 1
        for i in range(ord(square[0]) - 96, DIMENSION):
            for j in [-1, 1]:
                if 1 <= int(square[1]) + j*count <= DIMENSION:
                    squares.append((chr(i + 97), str(int(square[1]) + j*count)))
            count = count + 1

        count = 1
        for i in range(ord(square[0]) - 98, -1, -1):
            for j in [-1, 1]:
                if 1 <= int(square[1]) + j*count <= DIMENSION:
                    squares.append((chr(i + 97), str(int(square[1]) + j*count)))
            count = count + 1


    elif piece == 'R' or piece == 'r':
         for i in range(DIMENSION):
             if i+1 != int(square[1]):
                squares.append((square[0], str(i + 1)))

         for i in range(DIMENSION):
             if i!= ord(square[0]) - 97:
                squares.append((chr(i + 97), square[1]))

    elif piece == 'Q' or piece == 'q':
        count = 1
        for i in range(ord(square[0]) - 96, DIMENSION):
            for j in [-1, 1]:
                if 1 <= int(square[1]) + j*count <= DIMENSION:
                    squares.append((chr(i + 97), str(int(square[1]) + j*count)))
            count = count + 1

        count = 1

        for i in range(ord(square[0]) - 98, -1, -1):
            for j in [-1, 1]:
                if 1 <= int(square[1]) + j*count <= DIMENSION:
                    squares.append((chr(i + 97), str(int(square[1]) + j*count)))
            count = count + 1

        # Rook moves
        for i in range(DIMENSION):
             if i + 1 != int(square[1]):
                squares.append((square[0], str(i + 1)))

        for i in range(DIMENSION):
            if i != ord(square[0]) - 97:
                squares.append((chr(i + 97), square[1]))

    elif piece == 'K' or piece == 'k': 
        for i in [-1, 1]:
            if 0 <= ord(square[0]) - 97 + i < DIMENSION:
                squares.append((chr(ord(square[0]) + i), square[1]))
            if 1 <= int(square[1]) + i <= DIMENSION:
                squares.append((square[0], str( int(square[1]) + i)))

            for j in [-1, 1]:
                if 0 <= ord(square[0]) - 97 + i < DIMENSION and 1 <= int(square[1]) + j <= DIMENSION:
                    squares.append((chr(ord(square[0]) + i), str(int(square[1]) + j)))
        
    return squares

'''
class Actions:
    return

# Perform Alpha-Beta pruning search on a grid of Traffic Jam Puzzle
def Minimax(board):
    # Set up Minimax
    return

def actions(grid): 
    return

            
# Function to determine how beneficial a subsequent grid is to solving our problem
def heuristic(subGrid):
    return

def goal_test(state):
    return 

def isValid(coord):
    return 

def solution(node):

    return 
    '''
