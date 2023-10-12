import random

def create_board(n):
    board = [0] * (n*n)
    for i in range(n*n):
        board[i] = i + 1
    return board

def print_board(board):
    n = int(len(board) ** 0.5)
    for i in range(n):
        for j in range(n):
            print(board[i*n + j], end=" ")
        print()

def move_player(board, player, dice):
    new_position = (player + dice) % len(board)
    if new_position == 0:
        new_position = len(board)
    return new_position

def play_game(board, player1, player2):
    turn = 0
    while True:
        turn += 1
        print(f"Turn {turn}")
        print(f"Player {player1}'s turn")
        print_board(board)
        dice = random.randint(1, 6)
        print(f"Player {player1} rolled a {dice}")
        player1 = move_player(board, player1, dice)
        if player1 == len(board):
            print(f"Player {player1} wins!")
            break

        turn += 1
        print(f"Turn {turn}")
        print(f"Player {player2}'s turn")
        print_board(board)
        dice = random.randint(1, 6)
        print(f"Player {player2} rolled a {dice}")
        player2 = move_player(board, player2, dice)
        if player2 == len(board):
            print(f"Player {player2} wins!")
            break

def main():
    n = 10
    board = create_board(n)
    player1 = 1
    player2 = n*n - 1
    play_game(board, player1, player2)

if __name__ == "__main__":
    main()