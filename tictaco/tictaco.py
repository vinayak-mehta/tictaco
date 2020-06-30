# -*- coding: utf-8 -*-

import random


def render_grid(s):
    grid = "\n-----------------\n".join(
        [
            f"  {s[0]}  |  {s[1]}  |  {s[2]}\n (1) | (2) | (3)",
            f"  {s[3]}  |  {s[4]}  |  {s[5]}\n (4) | (5) | (6)",
            f"  {s[6]}  |  {s[7]}  |  {s[8]}\n (7) | (8) | (9)"
        ]
    )
    print(grid)


def check_win(s):
    _s = list(map(lambda x: x if x.strip() else "", s))

    # check columns
    for i in [0, 1, 2]:
        if _s[i]:
            if _s[i] == _s[i + 3] == _s[i + 6]:
                return _s[i]

    # check rows
    for i in [0, 3, 6]:
        if _s[i]:
            if _s[i] == _s[i + 1] == _s[i + 2]:
                return _s[i]

    # check diagonal 1
    if _s[0] and _s[0] == _s[4] == _s[8]:
        return _s[0]

    # check diagonal 2
    if _s[2] and _s[2] == _s[4] == _s[6]:
        return _s[2]

    return None


def get_o_turn(s):
    _s = list(map(lambda x: x if x.strip() else "", s))

    # check columns
    for i in [0, 1, 2]:
        idx_offset = {
            0: 0,
            1: 3,
            2: 6
        }

        column = [_s[i], _s[i + 3], _s[i + 6]]
        if column.count("x") == 2 and "" in column:
            return i + idx_offset[column.index("")] + 1

    # check rows
    for i in [0, 3, 6]:
        idx_offset = {
            0: 0,
            1: 1,
            2: 2
        }

        row = [_s[i], _s[i + 1], _s[i + 2]]
        if row.count("x") == 2 and "" in row:
            return i + idx_offset[row.index("")] + 1

    idx_offset = {
        0: 0,
        1: 4,
        2: 8
    }
    diagonal1 = [_s[0], _s[4], _s[8]]
    if diagonal1.count("x") == 2 and "" in diagonal1:
        return idx_offset[diagonal1.index("")] + 1

    idx_offset = {
        0: 2,
        1: 4,
        2: 6
    }
    diagonal2 = [_s[2], _s[4], _s[6]]
    if diagonal2.count("x") == 2 and "" in diagonal2:
        return idx_offset[diagonal2.index("")] + 1

    return random.randint(1, 9)


def human_vs_computer():
    s = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    turn = "x"
    render_grid(s)
    print(f"{turn} turn")

    while True:
        if turn == "x":
            i = int(input())
            if i not in list(range(1, 10)):
                print("Invalid input!")
                continue
        elif turn == "o":
            i = get_o_turn(s)

        i -= 1
        if s[i].strip():
            print("Slot taken!")
            continue

        s[i] = turn

        if turn == "x":
            turn = "o"
        else:
            turn = "x"

        print("\033c")
        render_grid(s)

        player = check_win(s)
        if player is not None:
            print(f"{player} wins! 🌮")
            break

        print(f"{turn} turn")

def human_vs_human():
    s = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    turn = "x"
    render_grid(s)
    print(f"{turn} turn")

    while True:
        i = int(input())
        if i not in list(range(1, 10)):
            print("Invalid input!")
            continue

        i -= 1
        if s[i].strip():
            print("Slot taken!")
            continue

        s[i] = turn

        if turn == "x":
            turn = "o"
        else:
            turn = "x"

        print("\033c")
        render_grid(s)

        player = check_win(s)
        if player is not None:
            print(f"{player} wins! 🌮")
            break

        print(f"{turn} turn")


def main():
    print("\033c")
    print("Welcome to tictaco! 🌮\n")
    print("Please select a game mode:\n")
    print("1. human vs computer")
    print("2. human vs human\n")
    game_mode = input("Enter game mode: ")

    if game_mode == "1":
        print("\033c")
        human_vs_computer()
    elif game_mode == "2":
        print("\033c")
        human_vs_human()
    else:
        raise ValueError("Invalid game mode!")
