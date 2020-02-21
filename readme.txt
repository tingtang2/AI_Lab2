# AI_Lab2

To run file: 
    python3 test.py

To run on the different grids:
    On line 45  of test.py, change initial_grid1 to initial_grid2 or initial_grid3

Structure of program:
    - A Board object keeps track of Piece insances. Information about a chess board and each piece are stored in
        Board and Piece objects respectively. For each Piece on in Board, the set of squares each piece can move to 
        is returned to the Board object so that it can generate the next possible boards. 

Program output:
The optimal move for given player considering given board
