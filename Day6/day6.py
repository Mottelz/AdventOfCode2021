from utils import read_and_explode_as_ints
from collections import Counter

CYCLE_LENGTH = 7
NEW_BORN_BONUS = 2


def age_pop(data: str, total_days) -> int:
    population = Counter(data)
    hatchery = {}
    for i in range(CYCLE_LENGTH):
        hatchery[i] = 0
    for day in range(1, total_days+1):
        pop_day = (day - 1) % CYCLE_LENGTH
        hatchery[(pop_day + NEW_BORN_BONUS) % CYCLE_LENGTH] = population[pop_day]
        population[pop_day] += hatchery[pop_day]
        hatchery[pop_day] = 0
    population.update(hatchery)
    print(population)
    return sum(population.values())


def main():
    data = read_and_explode_as_ints('input.txt', ',')
    print(f"Part 1: {age_pop(data, 80)}")
    print(f"Part 2: {age_pop(data, 256)}")


if __name__ == '__main__':
    main()
