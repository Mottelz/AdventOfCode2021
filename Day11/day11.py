from utils import read_and_explode_as_ints
from typing import List
from octopus import Octopus


def advance_neighbours(i: int, j: int, board: List[List[Octopus]]) -> List[List[Octopus]]:
    valid_i = [i]
    valid_j = [j]

    if i > 0:
        valid_i.append(i - 1)
    if i < len(board) - 1:
        valid_i.append(i + 1)

    if j > 0:
        valid_j.append(j - 1)
    if j < len(board[i]) - 1:
        valid_j.append(j + 1)

    for x in valid_i:
        for y in valid_j:
            if y == j and x == i:
                continue
            else:
                if board[x][y].needs_power():
                    board[x][y].increase()
                    if not board[x][y].needs_power():
                        board = advance_neighbours(x, y, board)
    return board


def advance_board(board: List[List[Octopus]]) -> List[List[Octopus]]:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].needs_power():
                board[i][j].increase()
                if not board[i][j].needs_power():
                    board = advance_neighbours(i, j, board)
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j].needs_power():
                count += 1
                board[i][j].reset()
    return count, board


def part1(board: List[List[Octopus]]) -> int:
    steps = 100
    out = 0
    for i in range(steps):
        results = advance_board(board)
        out += results[0]
        board = results[1]
    return out


def part2(board: List[List[Octopus]]) -> int:
    count = 0
    out = 0
    while count < 100:
        results = advance_board(board)
        count = results[0]
        board = results[1]
        out += 1
    return out


def construct_board(data: List[List[int]]) -> List[List[Octopus]]:
    out = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            temp.append(Octopus(data[i][j]))
        out.append(temp)
    return out


def main():
    data = read_and_explode_as_ints('input.txt')
    print(f"Part 1: {part1(construct_board(data))}")
    print(f"Part 2: {part2(construct_board(data))}")


if __name__ == '__main__':
    main()
