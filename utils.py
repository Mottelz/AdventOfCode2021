from typing import List


def read_file_by_line(filename: str) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def read_file_by_group(filename: str) -> List[str]:
    with open(filename) as file:
        data = file.read().replace('\n\n', '&&&').replace('\n', ' ').split('&&&')
    return data


def read_file_as_ints(filename: str) -> List[int]:
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(int(line))
    return data


def read_file_as_binaries(filename: str) -> List[int]:
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(int(line, 2))
    return data


def read_and_explode_as_ints(filename: str, split_char: str) -> List[int]:
    temp = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            temp = line.split(split_char)
    return [int(n) for n in temp]
