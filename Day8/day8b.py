from utils import read_file_by_line
from typing import List, Dict
from day8a import parse_line


def total_intersect(a: str, b: str) -> bool:
    return intersect(a, b) and intersect(b, a)


def intersect(a: str, b: str):
    for ca in a:
        if ca not in b:
            return False
    return True


def translate_output(alphabet: Dict[str, int], output: List[str]) -> int:
    temp = ''
    for a in output:
        for b in alphabet.keys():
            if total_intersect(a, b):
                temp += str(alphabet[b])
    return int(temp)


def part2(data: List[str]) -> int:
    total = 0
    for line in data:
        signals, output = parse_line(line)
        alphabet = parse_signals(signals)
        total += translate_output(alphabet, output)
    return total


def parse_signals(raw_signals: List[str]) -> Dict[int, str]:
    knowns = {}
    unknowns = raw_signals
    # Find the easy ones
    for sig in raw_signals:
        if len(sig) == 2:
            knowns.update({1: sig})
        elif len(sig) == 3:
            knowns.update({7: sig})
        elif len(sig) == 4:
            knowns.update({4: sig})
        elif len(sig) == 7:
            knowns.update({8: sig})
    unknowns = cleanup(knowns, unknowns)

    # Find 3
    for sig in unknowns:
        if len(sig) == 5 and contains_entire(superset=sig, subset=knowns[7]):
            knowns.update({3: sig})
    unknowns = cleanup(knowns, unknowns)

    # Find 9
    for sig in unknowns:
        if len(sig) == 6 and contains_entire(superset=sig, subset=knowns[3]):
            knowns.update({9: sig})
    unknowns = cleanup(knowns, unknowns)

    # Find 5
    for sig in unknowns:
        if len(sig) == 5 and contains_entire(superset=knowns[9], subset=sig):
            knowns.update({5: sig})
    unknowns = cleanup(knowns, unknowns)

    # Find 2
    for sig in unknowns:
        if len(sig) == 5:
            knowns.update({2: sig})
    unknowns = cleanup(knowns, unknowns)

    # Find 6
    for sig in unknowns:
        if contains_entire(superset=sig, subset=knowns[5]):
            knowns.update({6: sig})
    unknowns = cleanup(knowns, unknowns)

    knowns.update({0: unknowns[0]})

    return dict([(value, key) for key, value in knowns.items()])


def contains_entire(subset: str, superset: str) -> bool:
    for c in subset:
        if c not in superset:
            return False
    return True


def cleanup(knowns: Dict[int, str], unknowns: List[str]) -> List[str]:
    return list(filter(lambda u: u not in knowns.values(), unknowns))


def main():
    data = read_file_by_line('input.txt')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
