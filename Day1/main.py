from typing import List


def read_input(filename: str) -> List[int]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(int(line))
    return data


def is_bigger(prev: int, cur: int) -> bool:
    return prev < cur


def part1(numbers: List[int]) -> int:
    count = 0
    for i in range(1, len(numbers)):
        if is_bigger(numbers[i-1], numbers[i]):
            count += 1
    return count


def part2(numbers: List[int]) -> int:
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    d = numbers[3]
    sum1 = a+b+c
    sum2 = b+c+d
    count = is_bigger(sum1, sum2)
    for i in range(4, len(numbers)):
        a, b, c, d = b, c, d, numbers[i]
        sum1, sum2 = sum2, sum2+d-a
        if is_bigger(sum1, sum2):
            count += 1
    return count


def main():
    raw = read_input('input.txt')
    print(f"There are {part1(raw)} bigger than previous.")
    print(f"There are {part2(raw)} sums bigger than previous.")


if __name__ == '__main__':
    main()
