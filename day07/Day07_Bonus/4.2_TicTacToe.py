def tictactoe(rows,cols):
    size = rows *cols
    board = [" "] *size

    win_length = min(rows, cols)
    print("Board is", rows, "x", cols)
    print("To win, align", win_length, "symbols (row, column, or diagonal).")
    print()
    player = "X"
    while True:
        display_board(board, rows, cols)
        print("Player", player, "— choose a cell:")
        choice = input(">> ").strip()

        parts = choice.split(",")
        if len(parts) != 2:
            continue

        if not parts[0].strip().isdigit() or not parts[1].strip().isdigit():
            print("Please enter numbers.")
            continue

        r = int(parts[0].strip()) - 1
        c = int(parts[1].strip()) - 1

        if r < 0 or r >= rows or c < 0 or c >= cols:
            print("Out of range.")
            continue

        index = r * cols + c
        if board[index] != " ":
            print("Cell already taken.")
            continue
        board[index] = player
        if check_win(board, rows, cols, player, win_length):
            display_board(board, rows, cols)
            print("Player", player, "wins!")
            return

        if is_full(board):
            display_board(board, rows, cols)
            print("It's a draw!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"


def display_board(board, rows, cols):
    print()
    for r in range(rows):
        line = " "
        for c in range(cols):
            index = r * cols + c
            line = line + board[index]
            if c < cols - 1:
                line = line + " | "
        print(line)
        if r < rows - 1:
            separator = "---"
            for c in range(cols - 1):
                separator = separator + "+---"
            print(separator)
    print()


def check_win(board,rows,cols,player,win_length):
    for r in range(rows):    ##Lignes

        count = 0
        for c in range(cols):
            if board[r *cols + c] ==player:
                count =count + 1
                if count >=win_length:
                    return True
            else:
                count = 0
    for c in range(cols):                              ##Colonnes
        count = 0
        for r in range(rows):
            if board[r * cols + c] == player:
                count = count + 1
                if count >= win_length:
                    return True
            else:
                count = 0

    for r in range(rows - win_length + 1):    ##Diagonales descendantes 
        for c in range(cols - win_length + 1):
            count = 0
            for k in range(win_length):
                if board[(r + k) * cols + (c + k)] == player:
                    count = count + 1
                else:
                    break
            if count == win_length:
                return True

    for r in range(win_length - 1, rows):    ##Diagonales montantes 
        for c in range(cols - win_length + 1):
            count = 0
            for k in range(win_length):
                if board[(r - k) * cols + (c + k)] == player:
                    count = count + 1
                else:
                    break
            if count == win_length:
                return True

    return False


def is_full(board):
    for cell in board:
        if cell == " ":
            return False
    return True


if __name__ == "__main__":
    tictactoe(4, 4)