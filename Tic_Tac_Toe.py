def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def is_draw(board):
    return " " not in board


def play_game():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position! Choose between 1 and 9.")
                continue

            if board[move] != " ":
                print("Position already occupied!")
                continue

            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("🤝 It's a Draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")


while True:
    print("\n===== TIC TAC TOE =====")
    print("Positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    play_game()

    choice = input("Do you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("Thanks for playing!")
        break