from utils import read_file_by_line
from typing import List


def count_line(line: str, count: List[int]) -> List[int]:
    for i in range(len(line)):
        count[i] += 1 if line[i] == '1' else -1
    return count


def determine_frequency(data: List[str]) -> List[int]:
    count = [0] * len(data[0])
    for line in data:
        count = count_line(line, count)
    return count


def determine_frequency_at_position(data: List[str], pos: int) -> str:
    count = 0
    for line in data:
        count += 1 if line[pos] == '1' else -1
    return '0' if count < 0 else '1'


def part2(data: List[str]) -> int:
    co2_possibles = o2_possibles = data
    current_bit = 0
    while True:
        if len(co2_possibles) > 1:
            filter_bit = determine_frequency_at_position(co2_possibles, current_bit)
            co2_possibles = list(filter(lambda num: num[current_bit] != filter_bit, co2_possibles))
        if len(o2_possibles) > 1:
            filter_bit = determine_frequency_at_position(o2_possibles, current_bit)
            o2_possibles = list(filter(lambda num: num[current_bit] == filter_bit, o2_possibles))
        current_bit += 1
        if len(o2_possibles) == 1 and len(co2_possibles) == 1:
            break

    return int(o2_possibles[0], 2) * int(co2_possibles[0], 2)


def part1(data: List[str]) -> int:
    count = determine_frequency(data)
    least = most = ''

    for i in count:
        most += '1' if i > 0 else '0'
        least += '0' if i > 0 else '1'
    return int(most, 2) * int(least, 2)


def main():
    data = read_file_by_line('input.txt')
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
