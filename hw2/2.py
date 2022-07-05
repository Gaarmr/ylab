import random


offsets = [
    [(-1,  0), (1,  0)], 
    [( 0, -1), (0,  1)], 
    [(-1, -1), (1,  1)],
    [(-1,  1), (1, -1)],
]

BOARD = [
    list(range(10*i+1, 10*i+11)) for i in range(10)
]

print("*** Игра Крестики-нолики 10x10 ***" )


def draw_board(board):
    print("-" * 33)
    for y in range(10):
        print('|', '|'.join(f'{board[y][x]:>2}' for x in range(10)), '|')
    print("-" * 33)


def take_input(board, player_token):
    valid = False
    x = None
    y = None
    while not valid:
        if player_token == 'X':
            player_answer = input("Куда поставим " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except (ValueError, TypeError):
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= player_answer <= 100:
                y, x = divmod(player_answer-1, 10)
                if str(board[y][x]) not in "XO":
                    board[y][x] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
        else:
            x, y = random.choice([
                (x, y) 
                for y in range(10) 
                for x in range(10) 
                if str(board[y][x]) not in 'X0'
            ])
            board[y][x] = player_token
            valid = True
    return x, y


def check_win(board, x, y):
    for line in offsets:
        count = 1
        for x_off, y_off in line:
            new_x = x
            new_y = y
            while True:
                new_x += x_off
                new_y += y_off
                if new_x < 0 or new_x > 9 or new_y < 0 or new_y > 9:
                    break
                if board[new_y][new_x] != board[y][x]:
                    break
                count += 1
        if count >= 5:
            return True
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            player = "X"
        else:
            player = "0"
        x, y = take_input(board, player)
        counter += 1
        if counter > 4:
            tmp = check_win(board, x, y)
            if tmp:
                print(player, "выиграл!")
                win = True
                break
        if counter == 100:
            print("Ничья!")
            break
    draw_board(board)


main(BOARD)


input("Нажмите Enter для выхода!")
