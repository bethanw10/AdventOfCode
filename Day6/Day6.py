class OrbitMap:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def __repr__(self):
        return f"{self.name}"

    def find(self, name):
        if self.name == name:
            return self
        else:
            for child in self.children:
                match = child.find(name)

                if match is not None:
                    return match

        return None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    @property
    def orbit_count(self):
        return self.get_orbit_count()[0]

    def get_orbit_count(self):
        total = 0
        num_nodes = 1

        for child in self.children:
            child_total, num_child_nodes = child.get_orbit_count()
            total += child_total + num_child_nodes
            num_nodes += num_child_nodes

        return total, num_nodes

    def find_path(self, name):
        if self.name == name:
            return self
        else:
            for child in self.children:
                match = child.find(name)

                if match is not None:
                    return match

        return None

    def find_path_to(self, name, path_stack):
        if self.name == name:
            return self
        else:
            for child in self.children:
                match = child.find_path_to(name, path_stack)

                if match is not None:
                    path_stack.append(self.name)
                    return match

        return None

    def find_path_between(self, from_name, to_name):
        from_path_stack = []
        to_path_stack = []

        self.find_path_to(from_name, from_path_stack)
        self.find_path_to(to_name, to_path_stack)

        path = [path for path in from_path_stack if path not in to_path_stack] + \
               [path for path in to_path_stack if path not in from_path_stack]

        return path


def find(orbit_maps, planet):
    for orbit_map in orbit_maps:
        match = orbit_map.find(planet)
        if match is not None:
            return match

    return None


def main():
    file = open("input.txt", "r")
    data = file.read().split('\n')

    orbit_maps = []

    for orbit_data in data:
        planet, orbiter = orbit_data.split(')')

        planet_map = find(orbit_maps, planet)
        orbiter_map = find(orbit_maps, orbiter)

        if planet_map is None:
            planet_map = OrbitMap(planet)
            orbit_maps.append(planet_map)

        if orbiter_map is None:
            orbiter_map = OrbitMap(orbiter)
        else:
            orbit_maps.remove(orbiter_map)

        planet_map.add_child(orbiter_map)

    for orbit_map in orbit_maps:
        path_stack = orbit_map.find_path_between("YOU", "SAN")
        print(len(path_stack))


if __name__ == "__main__":
    main()
