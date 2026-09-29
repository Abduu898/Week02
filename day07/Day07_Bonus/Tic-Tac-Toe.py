def display_board(board):
    print()
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print()

def check_win(board, player):
    lines = [
        [1,2,3],[4,5,6],[7,8,9], # rows
        [1,4,7], [2,5,8],[3,6,9],# columns
        [1,5,9], [3,5,7],  # diagonals
    ]
    for line in lines:
        if board[line[0]] == player and board[line[1]] == player and board[line[2]] == player:
            return True
    return False

def is_full(board):
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True

def play():
    board = [" "] * 10      
    player = "X"

    while True:
        display_board(board)
        print("Player", player, "— choose a cell (1-9):")
        choice = input(">> ").strip()

        if not choice.isdigit():
            print("Please enter a number 1-9.")
            continue

        n = int(choice)
        if n < 1 or n > 9:
            print("Out of range. Choose 1-9.")
            continue

        if board[n] != " ":
            print("Cell already taken.")
            continue

        board[n] = player

        if check_win(board, player):
            display_board(board)
            print("Player", player, "wins!")
            return

        if is_full(board):
            display_board(board)
            print("It's a draw!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"
play()