import math


def calculate_fuel(num):
    return math.trunc(num / 3) - 2


if __name__ == "__main__":
    file = open("input.txt", "r")
    total = 0

    for line in file:
        total += calculate_fuel(int(line))

    print(total)
