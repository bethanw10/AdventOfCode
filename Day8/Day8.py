import math

WIDTH = 25
HEIGHT = 6
TOTAL_PIXELS = WIDTH * HEIGHT


def main():
    f = open("input.txt", "r")
    data = f.read()
    num_chars = len(data)

    lowest_zeros = None
    current_answer = None

    for i in range(1, math.trunc(num_chars / TOTAL_PIXELS)):

        num_digits = {'0': 0, '1': 0, '2': 0}

        for j in range(TOTAL_PIXELS):
            num_digits[data[(i * TOTAL_PIXELS) + j]] += 1

        if lowest_zeros is None or num_digits['0'] < lowest_zeros:
            lowest_zeros = num_digits['0']
            current_answer = num_digits['1'] * num_digits['2']

    print(current_answer)


if __name__ == "__main__":
    main()
