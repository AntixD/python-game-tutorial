def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def get_player_move():
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if row in range(0, 3) and col in range(0, 3):
                return row, col
            else:
                print("Invalid input. Please enter values between 1 and 3.")
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    move_count = 0

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        row, col = get_player_move()
        if board[row][col] == " ":
            board[row][col] = current_player
            move_count += 1
        else:
            print("This position is already taken. Please choose another.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if move_count == 9:
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
