from utils import read_and_explode_as_ints
from typing import List


def sum_dist(data: List[int], target: int) -> int:
    out = 0
    for n in data:
        out += abs(n-target)
    return out


def part1(data: List[int]) -> int:
    target_dist = sum_dist(data, data[0])
    for i in range(max(data)):
        temp = sum_dist(data, i)
        if temp < target_dist:
            target_dist = temp
    return target_dist


def calculate_cost(data: List[int], target: int) -> int:
    out = 0
    for n in data:
        out += sum(range(1, abs(n-target)+1))
    return out


def part2(data: List[int]) -> int:
    target_dist = calculate_cost(data, data[0])
    for i in range(max(data)):
        temp = calculate_cost(data, i)
        if temp < target_dist:
            target_dist = temp
    return target_dist


def main():
    data = read_and_explode_as_ints('input.txt', ',')
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == '__main__':
    main()