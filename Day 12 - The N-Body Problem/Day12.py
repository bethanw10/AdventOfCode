import math


class Moon:
    def __init__(self, x, y, z):
        self.pos = {'x': x, 'y': y, 'z': z}
        self.vel = {'x': 0, 'y': 0, 'z': 0}

    def __repr__(self):
        return \
            f"pos=<x={str(self.pos['x']).rjust(3, ' ')}, " \
            f"y={str(self.pos['y']).rjust(3, ' ')}, " \
            f"z={str(self.pos['z']).rjust(3, ' ')}>, " \
            f"vel=<x={str(self.vel['x']).rjust(3, ' ')}, " \
            f"y={str(self.vel['y']).rjust(3, ' ')}, " \
            f"z={str(self.vel['z']).rjust(3, ' ')}>"


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_pairs(array):
    pairs = []

    for i in range(len(array)):
        j = i + 1
        while j < len(array):
            pairs.append((array[i], array[j]))
            j += 1

    return pairs


def read_input(filename):
    moons = []

    with open(filename, 'r+') as file:
        content = file.read().split('\n')

    for line in content:
        positions = line[1:-1].split(", ")

        x, y, z = [int(position.split('=')[1]) for position in positions]

        moons.append(Moon(x, y, z))

    return moons


def run_cycle(moons, pairs):
    for moon_1, moon_2 in pairs:
        for pos in ['x', 'y', 'z']:

            if moon_1.pos[pos] > moon_2.pos[pos]:
                moon_1.vel[pos] -= 1
                moon_2.vel[pos] += 1
            elif moon_1.pos[pos] < moon_2.pos[pos]:
                moon_1.vel[pos] += 1
                moon_2.vel[pos] -= 1

    for moon in moons:
        for pos in ['x', 'y', 'z']:
            moon.pos[pos] += moon.vel[pos]

        # print(moon)


def run_cycles(moons, cycles):
    pairs = find_pairs(moons)

    for i in range(cycles):
        print()
        print(i + 1)
        run_cycle(moons, pairs)


def all_match(original, new):
    for i in range(len(new)):
        if original[i] != new[i]:
            return False

    return True


def num_steps_until_original(moons, pos):
    original = [(moon.pos[pos], moon.vel[pos]) for moon in moons]

    pairs = find_pairs(moons)
    i = 0

    while True:
        # print('\n', i)
        run_cycle(moons, pairs)
        i += 1

        if all_match(original, [(moon.pos[pos], moon.vel[pos]) for moon in moons]):
            return i


def calculate_energy(moons):
    total = 0

    for moon in moons:
        pos_total = 0
        vel_total = 0

        for pos in ['x', 'y', 'z']:
            pos_total += abs(moon.pos[pos])
            vel_total += abs(moon.vel[pos])

        total += (pos_total * vel_total)

    print('Total energy: ', total)


def main():
    moons = read_input('input.txt')

    x = num_steps_until_original(moons, 'x')
    y = num_steps_until_original(moons, 'y')
    z = num_steps_until_original(moons, 'z')

    print(lcm(x, lcm(y, z)))


if __name__ == "__main__":
    main()
