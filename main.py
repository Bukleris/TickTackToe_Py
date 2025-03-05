import random
#draw the game board
def printGameBoard(board):
    print("\n")
    print(f"  {board[7]} | {board[8]} | {board[9]}")
    print(" ---+---+---")
    print(f"  {board[4]} | {board[5]} | {board[6]}")
    print(" ---+---+---")
    print(f"  {board[1]} | {board[2]} | {board[3]}")
    print("\n")
