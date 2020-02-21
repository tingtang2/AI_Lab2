# AI_Lab2

To run file: 
    python3 test.py


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
