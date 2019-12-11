import csv


def add_coords_from_path(path, coords, current_pos):
    direction = path[0]
    number = int(path[1:])
    new_pos = current_pos

    for x in range(number):
        if direction == 'R':
            new_pos = (current_pos[0] + 1, current_pos[1])

        elif direction == 'L':
            new_pos = (current_pos[0] - 1, current_pos[1])

        elif direction == 'U':
            new_pos = (current_pos[0], current_pos[1] + 1)

        elif direction == 'D':
            new_pos = (current_pos[0], current_pos[1] - 1)

        coords.add(new_pos)
        current_pos = new_pos

    return current_pos


def get_coords_for_wire(wire):
    coords = set()
    current_pos = (0, 0)

    for path in wire:
        current_pos = add_coords_from_path(path, coords, current_pos)

    return coords


def main():
    file = open("input.txt", "r")
    csv_reader = csv.reader(file, delimiter=',')

    wire_1 = next(csv_reader)
    wire_2 = next(csv_reader)

    wire_1_coords = get_coords_for_wire(wire_1)
    wire_2_coords = get_coords_for_wire(wire_2)

    intersections = {coords for coords in wire_1_coords if coords in wire_2_coords}

    shortest_distance = None
    shortest_coords = None

    for intersection in intersections:
        distance = intersection[0] + intersection[1]

        if shortest_distance is None or distance < shortest_distance:
            shortest_distance = distance
            shortest_coords = intersection

    print(shortest_distance)


if __name__ == "__main__":
    main()

