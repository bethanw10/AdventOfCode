WIDTH = 25
HEIGHT = 6
PIXELS_PER_LAYER = WIDTH * HEIGHT


def chunks(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]


def print_image(image):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == '0':
                print('⬛', end='')
            else:
                print('⬜', end='')
        print()


def part_1(data):
    lowest_zeros = None
    current_answer = None

    for layer in chunks(data, PIXELS_PER_LAYER):
        num_digits = {'0': 0, '1': 0, '2': 0}

        for pixel in layer:
            num_digits[pixel] += 1

        if lowest_zeros is None or num_digits['0'] < lowest_zeros:
            lowest_zeros = num_digits['0']
            current_answer = num_digits['1'] * num_digits['2']

    print(current_answer)


def part_2(data):
    image = [['2' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for layer in chunks(data, PIXELS_PER_LAYER):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pixel = layer[x + (y * WIDTH)]

                if image[y][x] == '2':
                    image[y][x] = pixel

    print_image(image)


def main():
    f = open("input.txt", "r")
    part_2(f.read())


if __name__ == "__main__":
    main()
