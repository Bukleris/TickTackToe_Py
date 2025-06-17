import random
##Define engines
# game board engine 
def printGameBoard(board):
    print("\n")
    print(f"  {board[7]} | {board[8]} | {board[9]}")
    print(" ---+---+---")
    print(f"  {board[4]} | {board[5]} | {board[6]}")
    print(" ---+---+---")
    print(f"  {board[1]} | {board[2]} | {board[3]}")
    print("\n")

# game win combinations 
def check_winner(board, symbol):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == symbol for i in combo):
            return True
    return False

# full board engine
def is_board_full(board):
    return all(spot in ['X', 'O'] for spot in board.values())

# game flip coin engine 
def flip_coin():
    return random.choice(['heads', 'number'])

# replay function engine
def replay():
    choice = input("Play again? Enter Yes or No: ")
    if choice.lower() == 'yes' or choice.lower() == 'y':
        return True
    else:
        return False

## Main game 
def main():
    print('Welcome to Tic Tac Toe')
    
    # Get player names
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
    ### Game setup
    while True:
        #  print new board each game
        board = {i: ' ' for i in range(1, 10)}
        
        # flip whoes goes first
        choice = input(f"{player1}, choose heads or number: ").lower()
        coin_flip = flip_coin()
        
        if coin_flip == choice:
            current_player = player1
        else:
            current_player = player2
        
        print(f"Coin flip: {coin_flip}. {current_player} goes first!")
       
        # symbols selection
        symbol_choice = input(f"{current_player}, choose your symbol (X or O): ").upper()
        if symbol_choice == 'X':
            player_symbols = {player1: 'X', player2: 'O'}
        else:
            player_symbols = {player1: 'O', player2: 'X'}
        
        # print empty board
        printGameBoard(board)
        
        # GAME PLAY LOOP
        while True:
            # Players moves
            move = int(input(f"{current_player}, enter a number to place your symbol: "))
            
            # Check if spot is empty
            if board[move] == ' ':
                board[move] = player_symbols[current_player]
            else:
                print("That spot is already taken. Try again.")
                continue
            
            # print board after move    
            printGameBoard(board)
            
            # Check winner
            if check_winner(board, player_symbols[current_player]):
                print(f"{current_player} wins!")
                break
            
            # Check full board 
            if is_board_full(board):
                print("It's a tie!")
                break
            
            # Switch to other player
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
        
        # replay 
        if not replay():
            print("Thanks for playing!")
            break

#run the game
if __name__ == "__main__":
    main()
