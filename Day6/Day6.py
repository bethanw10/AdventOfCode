class OrbitMap:
    def __init__(self, name, children=None):
        self.name = name

        if children is not None:
            self.children = children
        else:
            self.children = []

    def __repr__(self):
        return f"{self.name}: {[child for child in self.children]}"

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

    def get_orbit_count(self):
        total = len(self.children)

        for child in self.children:
            total += (child.get_orbit_count() * 2)

        return total


def find(orbit_maps, planet):
    for orbit_map in orbit_maps:
        match = orbit_map.find(planet)
        if match is not None:
            return match

    return None


def main():
    file = open("input-test.txt", "r")
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
        print(orbit_map)

    print(orbit_maps[0].get_orbit_count())


if __name__ == "__main__":
    main()
