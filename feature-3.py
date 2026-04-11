def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    steps = 0

    print("--- Крестики-нолики ---")
    
    while steps < 9:
        print_board(board)
        try:
            row = int(input(f"Игрок {current_player}, выберите строку (0, 1, 2): "))
            col = int(input(f"Игрок {current_player}, выберите столбец (0, 1, 2): "))
            
            if board[row][col] != " ":
                print("Эта клетка уже занята! Попробуйте снова.")
                continue
        except (ValueError, IndexError):
            print("Ошибка ввода! Введите числа от 0 до 2.")
            continue

        board[row][col] = current_player
        steps += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Поздравляем! Игрок {current_player} победил!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("Ничья!")

if __name__ == "__main__":
    tic_tac_toe()
