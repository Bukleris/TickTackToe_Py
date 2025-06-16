import random
#players 
def main():
    board = {i: ' ' for i in range(1, 10)} #creates a dictionary where number becomes a key
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
#who start first 
    choice = input(f"{player1}, choose heads or number: ").lower()
    coin_flip = flip_coin()
    
    if coin_flip == choice:
        current_player = player1
    else:
        current_player = player2
    
    print(f"Coin flip: {coin_flip}. {current_player} goes first!")

#symbol for tic tac toe selection
    
    symbol_choice = input(f"{current_player}, choose your symbol (X or O): ").upper()
    if symbol_choice == 'X':
        player_symbols = {player1: 'X', player2: 'O'}
    else:
        player_symbols = {player1: 'O', player2: 'X'}
#start
    printGameBoard(board)
#turns solution
    while True:
        move = int(input(f"{current_player}, enter a number to place your symbol: "))
        if board[move] == ' ':
            board[move] = player_symbols[current_player]
        else:
            print("That spot is already taken. Try again.")
            continue
#print after move
        printGameBoard(board)

        if check_winner(board, player_symbols[current_player]):
            print(f"{current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = player1 if current_player == player2 else player2
#call the game
if __name__ == "__main__":
    main()
