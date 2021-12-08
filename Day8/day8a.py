from utils import read_file_by_line
from typing import List
SEGMENTS = ['a', 'b', 'c', 'd', 'e', 'f']


def part1(data: List[str]) -> int:
    count = 0
    for line in data:
        signals, output = parse_line(line)
        for i in output:
            if len(i) in [2, 3, 4, 7]:
                count += 1
    return count


def parse_line(raw: str) -> (List[str], List[str]):
    raw_signals = raw.split("|")[0]
    raw_output = raw.split("|")[1]
    return raw_signals.strip().split(), raw_output.strip().split()


def main():
    data = read_file_by_line('input.txt')
    print(f"Part 1: {part1(data)}")


if __name__ == '__main__':
    main()
