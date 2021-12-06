from utils import read_and_explode_as_ints
from collections import Counter

TOTAL_DAYS = 80 # Change this number for day
CYCLE_LENGTH = 7
NEW_BORN_BONUS = 2


def part1(data: str) -> int:
    population = Counter(data)
    hatchery = {}
    for i in range(CYCLE_LENGTH):
        hatchery[i] = 0
    for day in range(1, TOTAL_DAYS+1):
        pop_day = (day - 1) % CYCLE_LENGTH
        hatchery[(pop_day + NEW_BORN_BONUS) % CYCLE_LENGTH] = population[pop_day]
        population[pop_day] += hatchery[pop_day]
        hatchery[pop_day] = 0
    population.update(hatchery)
    print(population)
    return sum(population.values())


def main():
    data = read_and_explode_as_ints('input.txt', ',')
    print(f"{part1(data)}")


if __name__ == '__main__':
    main()
