from utils import read_file_by_line
from typing import List


def process_instruction_for_part1(direction: str, magnitude: int, depth: int, horizontal: int) -> (int, int):
    if direction == 'forward':
        horizontal += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude
    return depth, horizontal


def process_instruction_for_part2(direction: str, magnitude: int, depth: int, horizontal: int, aim: int) -> (int, int):
    if direction == 'forward':
        horizontal += magnitude
        depth += magnitude*aim if aim != 0 else 0
    elif direction == 'down':
        aim += magnitude
    elif direction == 'up':
        aim -= magnitude
    return depth, horizontal, aim


def parse_instruction(raw: str) -> (str, int):
    out = raw.split()
    return out[0], int(out[1])


def part1(data: List[str]) -> int:
    depth = horizontal = 0
    for instruction in data:
        direction, magnitude = parse_instruction(instruction)
        depth, horizontal = process_instruction_for_part1(direction, magnitude, depth, horizontal)
    return depth*horizontal


def part2(data: List[str]) -> int:
    depth = horizontal = aim = 0
    for instruction in data:
        direction, magnitude = parse_instruction(instruction)
        depth, horizontal, aim = process_instruction_for_part2(direction, magnitude, depth, horizontal, aim)
    return depth*horizontal


def main():
    data = read_file_by_line("input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
