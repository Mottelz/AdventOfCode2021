from typing import List
from utils import read_file_as_ints


def is_bigger(prev: int, cur: int) -> bool:
    return prev < cur


def part1(numbers: List[int]) -> int:
    count = 0
    for i in range(1, len(numbers)):
        if is_bigger(numbers[i-1], numbers[i]):
            count += 1
    return count


def part2(numbers: List[int]) -> int:
    sum1 = numbers[0] + numbers[1] + numbers[2]
    sum2 = numbers[1] + numbers[2] + numbers[3]
    count = is_bigger(sum1, sum2)
    for i in range(4, len(numbers)):
        sum1, sum2 = sum2, sum2 + numbers[i] - numbers[i-3]
        if is_bigger(sum1, sum2):
            count += 1
    return count


def main():
    raw = read_file_as_ints('input.txt')
    print(f"There are {part1(raw)} bigger than previous.")
    print(f"There are {part2(raw)} sums bigger than previous.")


if __name__ == '__main__':
    main()
