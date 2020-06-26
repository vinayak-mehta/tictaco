# -*- coding: utf-8 -*-


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


def main():
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
