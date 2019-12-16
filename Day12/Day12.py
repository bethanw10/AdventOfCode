class Moon:
    def __init__(self, x, y, z):
        self.pos_x, self.pos_y, self.pos_z = x, y, z
        self.vel_x, self.vel_y, self.vel_z = 0, 0, 0

    def __repr__(self):
        return \
            f"pos=<x={str(self.pos_x).rjust(3, ' ')}, " \
            f"y={str(self.pos_y).rjust(3, ' ')}, " \
            f"z={str(self.pos_z).rjust(3, ' ')}>, " \
            f"vel=<x={str(self.vel_x).rjust(3, ' ')}, " \
            f"y={str(self.vel_y).rjust(3, ' ')}, " \
            f"z={str(self.vel_z).rjust(3, ' ')}>"


def read_input():
    moons = []

    with open('input.txt', 'r+') as file:
        content = file.read().split('\n')

    for line in content:
        positions = line[1:-1].split(", ")

        x, y, z = [int(position.split('=')[1]) for position in positions]

        moons.append(Moon(x, y, z))

    return moons


def main():
    moons = read_input()

    for moon in moons:
        print(moon)


if __name__ == "__main__":
    main()
