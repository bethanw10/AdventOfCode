import csv


def main_part_1():
    file = open("input.txt", "r")
    csv_reader = csv.reader(file, delimiter=',')

    wire_1_coords = get_coords_for_wire(next(csv_reader))
    wire_2_coords = get_coords_for_wire(next(csv_reader))

    intersections = set(wire_1_coords).intersection(set(wire_2_coords))

    shortest_distance = None

    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])

        if shortest_distance is None or distance < shortest_distance:
            shortest_distance = distance

    print(shortest_distance)


def add_coords_from_path(coords, path, current_pos):
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

        coords.append(new_pos)
        current_pos = new_pos

    return current_pos


def get_coords_for_wire(wire):
    coords = []
    current_pos = (0, 0)

    for path in wire:
        current_pos = add_coords_from_path(coords, path, current_pos)

    return coords


def main_part_2():
    file = open("input.txt", "r")
    csv_reader = csv.reader(file, delimiter=',')

    wire_1 = next(csv_reader)
    wire_2 = next(csv_reader)

    wire_1_coords = get_coords_for_wire(wire_1)
    wire_2_coords = get_coords_for_wire(wire_2)

    intersections = set(wire_1_coords).intersection(set(wire_2_coords))

    lowest_step_count = None

    for intersection in intersections:
        steps_1 = wire_1_coords.index(intersection) + 1
        steps_2 = wire_2_coords.index(intersection) + 1

        step_count = steps_1 + steps_2

        if lowest_step_count is None or step_count < lowest_step_count:
            lowest_step_count = step_count

    print(lowest_step_count)


if __name__ == "__main__":
    main_part_2()