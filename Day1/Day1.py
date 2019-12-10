import math


def calculate_fuel(num):
    return math.trunc(num / 3) - 2


def calculate_fuel_part_2(num, total):
    fuel_cost = math.trunc(num / 3) - 2

    if fuel_cost >= 1:
        total += fuel_cost
        return calculate_fuel_part_2(fuel_cost, total)

    return total


def main():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        total += calculate_fuel_part_2(int(line), 0)

    print(total)


if __name__ == "__main__":
    main()
