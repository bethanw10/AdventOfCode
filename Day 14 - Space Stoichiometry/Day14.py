import math


class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} {self.name}"


class Recipe:
    def __init__(self, output, ingredients: [Ingredient]):
        self.output = output
        self.ingredients = ingredients

    def __repr__(self):
        return f"{self.output} => {self.ingredients}"


def load_recipes(content):
    lines = content.split('\n')

    recipes = {}

    for line in lines:
        ingredients, result = line.split(' => ')

        result_amount, result_name = tuple(result.split(' '))

        ingredients_list = []

        for ingredient in ingredients.split(', '):
            amount, name = ingredient.split(' ')
            ingredients_list.append(Ingredient(name, int(amount)))

        recipes[result_name] = Recipe(int(result_amount), ingredients_list)

    return recipes


def get_ore_needed(recipes, name, amount):
    needed = {name: amount}
    leftovers = {}

    while list(needed.keys()) != ['ORE']:
        for target_name, target_needed in list(needed.items()):
            if target_name == 'ORE':
                continue

            if target_name in leftovers:
                if leftovers[target_name] > needed[target_name]:
                    leftovers[target_name] -= needed[target_name]
                    needed[target_name] = 0
                else:
                    needed[target_name] -= leftovers[target_name]
                    leftovers[target_name] = 0
            else:
                leftovers[target_name] = 0

            amount_needed = needed[target_name]
            output = recipes[target_name].output

            num_repeats = math.ceil(amount_needed / output)
            leftovers[target_name] += (output * num_repeats) - amount_needed

            for ingredient in recipes[target_name].ingredients:
                if ingredient.name not in needed:
                    needed[ingredient.name] = 0

                needed[ingredient.name] += (ingredient.amount * num_repeats)

            del needed[target_name]

    return needed['ORE']


def part_2(recipes):
    lowest = 443537  # Makes 1
    highest = 5_000_000_000
    mid = 0

    target = 1_000_000_000_000
    found = False

    while not found:
        mid = (lowest + highest) // 2
        output = get_ore_needed(recipes, 'FUEL', mid)

        if lowest == highest + 1:
            return mid

        if output == target:
            found = True
        elif target < output:
            highest = mid - 1
        else:
            lowest = mid + 1

    return mid


def main():
    f = open("input.txt", "r")
    content = f.read()

    recipes = load_recipes(content)

    print(get_ore_needed(recipes, 'FUEL', 1))

    print(part_2(recipes))


if __name__ == "__main__":
    main()
