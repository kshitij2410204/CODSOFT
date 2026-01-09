board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def play_game():
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Player X and Player O")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
            if board[move] != " ":
                print("Position already taken. Try again.")
                continue
            board[move] = current_player
            print_board()

            if check_winner(current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            if is_draw():
                print("🤝 It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        except:
            print("Invalid input. Enter number 1-9.")

play_game()
