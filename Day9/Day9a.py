from typing import List
from utils import read_file_by_line


def is_low_point(p: int, neighbour_values: List[int]) -> bool:
    for n in neighbour_values:
        if n <= p:
            return False
    return True


def get_neighbours(i: int, j: int, board: List[List[int]]) -> List[int]:
    out = []
    if i > 0:
        out.append(board[i-1][j])
    if i < len(board) - 1:
        out.append(board[i+1][j])
    if j > 0:
        out.append(board[i][j-1])
    if j < len(board[i]) - 1:
        out.append(board[i][j+1])
    return out


def create_board(data: List[str]) -> List[List[str]]:
    out = []
    for line in data:
        out.append([int(n) for n in line])
    return out


def part1(data: List[str]) -> int:
    out = 0
    board = create_board(data)
    print(board)
    for x in range(len(board)):
        for y in range(len(board[x])):
            neighbours = get_neighbours(x, y, board)
            cell_value = board[x][y]
            if is_low_point(cell_value, neighbours):
                out += 1 + board[x][y]
    return out


def main():
    data = read_file_by_line('input.txt')
    print(f"Part 1: {part1(data)}")


if __name__ == '__main__':
    main()