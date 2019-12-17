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


def find_pairs(array):
    for i in range(len(array)):
        j = i + 1
        while j < len(array):
            yield(array[i], array[j])
            j += 1


def read_input():
    moons = []

    with open('input.txt', 'r+') as file:
        content = file.read().split('\n')

    for line in content:
        positions = line[1:-1].split(", ")

        x, y, z = [int(position.split('=')[1]) for position in positions]

        moons.append(Moon(x, y, z))

    return moons


def run_cycle(moons):
    pairs = find_pairs(moons)

    for moon_1, moon_2 in pairs:
        for pos in ['x', 'y', 'z']:
            moon_1.vel[pos] += 1 if moon_2.pos[pos] > moon_1.pos[pos] else -1
            moon_2.vel[pos] += -1 if moon_1.pos[pos] > moon_2.pos[pos] else 1

    for moon in moons:
        for pos in ['x', 'y', 'z']:
            moon.pos[pos] += moon.vel[pos]


def main():
    moons = read_input()

    for i in range(1000):
        run_cycle(moons)

    total = 0

    for moon in moons:
        pos_total = 0
        vel_total = 0

        for pos in ['x', 'y', 'z']:
            pos_total += abs(moon.pos[pos])
            vel_total += abs(moon.vel[pos])

        total += (pos_total * vel_total)

    print(total)


if __name__ == "__main__":
    main()
