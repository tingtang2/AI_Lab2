### Main file to simulate the Traffic Jam puzzle
### Ting Chen and Yanish Rambocus
### Lab 2 CMSC 395 Artificial Intelligence

import copy

DIMENSION = 8
MAX_DEPTH = 4
TURN = "white"

# Rieman values for pieces for use by H-Minimax 
pieceMap = {"p": -1, "P": 1, "n": -3, "N": 3,
            "b": -3, "B": 3, "r": -5, "R": 5,
            "q": -9, "Q": 9, "k": 0, "K": 0}
if TURN == "black":
    pieceMap = {"p": 1, "P":-1, "n": 3, "N": -3,
                "b": 3, "B": -3, "r": 5, "R": -5,
                "q": 9, "Q": -9, "k": 0, "K": 0}


# Object defining a chess board and use it's properties
class Board:

    def __init__(self, board, turn=TURN, prevBoard=None, move=None):

        self.board = board
        self.myBoard = []
        self.prevBoard = prevBoard
        self.turn = turn
        self.value = None
        self.move = move

        # Added pieces to list 
        self.pieces = []

        # Create Piece instances and add them to myBoard
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

    # Get actual coordinates of the grid as opposed to chess coordinates 
    def getCoord(self, square):
        return (8 - int(square[1]), ord(square[0]) - 97)

    def getPieceOnSquare(self, square):
        return self.myBoard[self.getCoord(square)[0]][self.getCoord(square)[1]]

    def getPieces(self):
        return self.pieces

    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val

    def getMove(self):
        return self.move
    
    def getTurn(self):
        return self.turn

    # Generate next possible boards from given board
    def getNextBoards(self):
        boards = []
        for piece in self.pieces:
            if piece.getColor() == self.turn:  

                for square in piece.getMoveSquares(self):
                    canMove = False
                    move = None
                    coords = self.getCoord(square)

                    if self.myBoard[coords[0]][coords[1]] is None:
                        canMove = True
                    else:
                        if self.myBoard[coords[0]][coords[1]].getPiece().islower() and self.turn == "white" or \
                                self.myBoard[coords[0]][coords[1]].getPiece().isupper() and self.turn == "black":
                            canMove = True

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

        return boards

    # Returns whether a move has put the the player's king in check
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

        
# Piece object to keep track of properties of a piece and generate squares it can move to on a given board
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

    # Generate squares a piece can move to depending on it's nature
    def getMoveSquares(self, board):
        squares = []

        if self.piece == 'P':
            coord = board.getCoord(self.getSquare())
            if int(self.square[1]) + 1 < DIMENSION:
                if board.getPieceOnSquare((self.square[0], str(int(self.square[1]) + 1))) == None:
                    squares.append((self.square[0], str(int(self.square[1]) + 1)))
                if coord[1] - 1 > 0:
                    square = (chr(ord(self.square[0]) - 1), str(int(self.square[1]) + 1))
                    if board.getPieceOnSquare(square) != None: 
                        if board.getPieceOnSquare(square).getColor() == "black":
                            squares.append(square)
                if coord[1] + 1 < DIMENSION:
                    square = (chr(ord(self.square[0]) + 1), str(int(self.square[1]) + 1))
                    if board.getPieceOnSquare(square) != None:
                        if board.getPieceOnSquare(square).getColor() == "black":
                            squares.append(square)

        elif self.piece == 'p':
            coord = board.getCoord(self.getSquare())
            if int(self.square[1]) - 1 > 0:
                if board.getPieceOnSquare((self.square[0], str(int(self.square[1]) - 1))) == None:
                    squares.append((self.square[0], str(int(self.square[1]) - 1)))
                if coord[1] - 1 > 0:
                    square = (chr(ord(self.square[0]) - 1), str(int(self.square[1]) - 1))
                    if board.getPieceOnSquare(square) != None: 
                        if board.getPieceOnSquare(square).getColor() == "white":
                            squares.append(square)
                if coord[1] + 1 < DIMENSION:
                    square = (chr(ord(self.square[0]) + 1), str(int(self.square[1]) - 1))
                    if board.getPieceOnSquare(square) != None:
                        if board.getPieceOnSquare(square).getColor() == "white":
                            squares.append(square)

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
                if count <= 0:
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
                if count <= 0:
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
                if count <= 0:
                    break
                if board.getPieceOnSquare(square) == None:
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
                #print(square[0], square[1])
                if count <= 0:
                    break
                if board.getPieceOnSquare(square) == None:
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
                #print(square[0], square[1])
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

        return squares


# H-Minimax function to explore further states
def H_Minimax(board):
    # Set up Minimax
    frontier = []
    v = max_value(board, float("-inf"), float("inf"), 0, frontier)
    board.setValue(v)
    print("frontier", len(frontier))
    frontier = frontier[1:]

    best_action = None
 
    for b in frontier:
        if b.getValue() == v:
            best_action = b.getMove()
            break

    return v, best_action

# max_value to determine which branch to explore. Used by H-Minimax
def max_value(board, alpha, beta, depth, front):
    if depth == MAX_DEPTH:
        val = Eval(board, depth)
        board.setValue(val)
        front.insert(0, board)
        return val

    v = float("-inf")
    i = 0
    for b in largestPiecePolicy(board):
    #for b in closestPiecePolicy(board):
        newDepth = depth + 1
        v = max(v, min_value(b, alpha, beta, newDepth, front))
        if v >= beta:
            board.setValue(v)
            front.insert(0, board)
            return v
        alpha = max(alpha, v)
        i += 1
    
    board.setValue(v)
    front.insert(0, board)
    return v

# min_value to determine which branch to explore. Used by H-Minimax
def min_value(board, alpha, beta, depth, front):
    if depth == MAX_DEPTH:
        val = Eval(board, depth)
        board.setValue(val)
        front.insert(0, board)
        return val

    v = float("inf")
    i = 0
    for b in largestPiecePolicy(board):
    #for b in closestPiecePolicy(board):
        newDepth = depth + 1
        v = min(v, max_value(b, alpha, beta, newDepth, front))
        if v <= alpha:
            board.setValue(v)
            front.insert(0, board)
            return v
        beta = min(beta, v)
        i += 1
    
    board.setValue(v)
    front.insert(0, board)
    return v

# Evaluates score of board
def Eval(board, d):
    value = 0

    for piece in board.getPieces():
        value += pieceMap[piece.getPiece()]

    checkmate = 0
    if len(board.getNextBoards()) == 0:
        for piece in board.getPieces():
            checkmate += abs(pieceMap[piece.getPiece()])

    if board.getTurn() == "black":
        checkmate = -checkmate
        
    return value + checkmate -d

#Exploration policies
def largestPiecePolicy(board):
    return sorted(board.getNextBoards(), key=lambda x: pieceMap[x.getMove()[0]], reverse=True)

def closestPiecePolicy(board):
    return sorted(board.getNextBoards(), key=lambda x: x.getMove()[-1], reverse=True)
