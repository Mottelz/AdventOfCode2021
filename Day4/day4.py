from typing import List
from utils import read_and_explode_as_ints, read_file_by_line
from board import Board


def create_boards(data: List[str]) -> List[Board]:
    out = []
    temp = []
    for line in data:
        if line == '':
            out.append(Board(temp))
            temp = []
        else:
            a = line.strip()
            temp.append([int(n) for n in list(filter(lambda x: x != '', line.split(' ')))])
    return out


def play_bingo(balls: List[int], boards: List[Board]) -> (int, Board):
    for ball in balls:
        for board in boards:
            board.mark(ball)
            if board.check_for_win():
                return ball, board


def lose_bingo(balls: List[int], boards: List[Board]) -> (int, Board):
    losing_board = find_loser(balls, boards)
    for ball in balls:
        losing_board.mark(ball)
        if losing_board.check_for_win():
            return ball, losing_board


def find_loser(balls: List[int], boards: List[Board]) -> Board:
    for ball in balls:
        for board in boards:
            board.mark(ball)
        remaining_losers = list(filter(lambda b: not b.check_for_win(), boards))
        if len(remaining_losers) == 1:
            return remaining_losers[0]


def part1(balls: List[int], raw_boards: List[str]) -> int:
    boards = create_boards(raw_boards)
    last_ball, winning_board = play_bingo(balls, boards)
    # print(f"ball is: {last_ball}\n{winning_board}")
    return last_ball * len(winning_board)


def part2(balls: List[int], raw_boards: List[str]) -> int:
    boards = create_boards(raw_boards)
    last_ball, losing_board = lose_bingo(balls, boards)
    # print(f"ball is: {last_ball}\n{losing_board}")
    return last_ball * len(losing_board)


def main():
    balls = read_and_explode_as_ints('input-balls.txt', ',')
    raw_boards = read_file_by_line('input-boards.txt')
    print(f"part 1: {part1(balls, raw_boards)}")
    print(f"part 2: {part2(balls, raw_boards)}")


if __name__ == "__main__":
    main()
