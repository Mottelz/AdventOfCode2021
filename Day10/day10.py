from utils import read_file_by_line
from typing import List
from collections import deque
PAIRS = {'}': '{', '>': '<', ')': '(', ']': '['}
PAIRS_FLIPPED = {'{': '}', '<': '>', '(': ')', '[': ']'}
ERROR_COST = {'>': 25137, '}': 1197, ']': 57, ')': 3}
COMPLETENESS_COST = {'>': 4, '}': 3, ']': 2, ')': 1}


def get_error_value(line: str) -> int:
    stack = deque()
    for c in line:
        if c in PAIRS.values():
            stack.append(c)
        elif PAIRS[c] != stack.pop():
            return ERROR_COST[c]
    return 0


def get_complete_cost(line: str) -> int:
    stack = deque()
    out = 0
    for c in line:
        if c in PAIRS.values():
            stack.append(c)
        elif PAIRS[c] == stack[-1]:
            stack.pop()

    while len(stack) > 0:
        out *= 5
        out += COMPLETENESS_COST[PAIRS_FLIPPED[stack.pop()]]
    return out


def part1(data: List[str]):
    out = 0
    for line in data:
        out += get_error_value(line)
    return out


def part2(data: List[str]):
    scores = []
    for line in data:
        if get_error_value(line) == 0:
            scores.append(get_complete_cost(line))
    return sorted(scores)[(len(scores)-1)//2]


def main():
    data = read_file_by_line('input.txt')
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
