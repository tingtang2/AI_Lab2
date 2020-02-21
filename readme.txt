# AI_Lab2

To run file: 
    python3 test.py

To run on the different grids:
    On line 45  of test.py, change board1 to board2 or board3 to run the program on the different inital boards provided
    Each board is hard coded from lines 

Structure of program:
    - A Board object keeps track of Piece insances. Information about a chess board and each piece are stored in
        Board and Piece objects respectively. For each Piece on in Board, the set of squares each piece can move to 
        is returned to the Board object so that it can generate the next possible boards. 

    - An isCheck() method determines whether a board resulted from a legal move since if it is a player to move,
      they cannot put their king in check

    - H-Minimax evalutes the generated boards using Alpha Beta Pruning with a max-depth of 4 to decide which 
      boards to explore wit

    - Running test.py outputs the best move for a given player

Program output:
    The optimal move for given player considering given board
