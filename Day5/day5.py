from line import Line, Point
import typing as t
from collections import Counter
from utils import read_file_by_line


def get_points(line: str) -> (Point, Point):
    temp = line.split(' -> ')
    start = Point(int(temp[0].split(',')[0]), int(temp[0].split(',')[1]))
    end = Point(int(temp[1].split(',')[0]), int(temp[1].split(',')[1]))
    if start.x > end.x or start.y > end.y:
        start, end = end, start
    return start, end


def part2(data: t.List[str]) -> int:
    heatmap = Counter()
    count = 0

    for line in data:
        start, end = get_points(line)
        dist_x, dist_y = abs(start.x - end.x), abs(start.y - end.y)
        if start.x == end.x or start.y == end.y or dist_x == dist_y:
            heatmap.update(Line(start, end).list())
    for p, c in heatmap.items():
        count += 1 if c > 1 else 0
    return count


def part1(data: t.List[str]) -> int:
    heatmap = Counter()
    count = 0
    for line in data:
        start, end = get_points(line)
        if start.x == end.x or start.y == end.y:
            heatmap.update(Line(start, end).list())
    for p, c in heatmap.items():
        count += 1 if c > 1 else 0
    return count


def main():
    data = read_file_by_line('input.txt')
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == '__main__':
    main()
