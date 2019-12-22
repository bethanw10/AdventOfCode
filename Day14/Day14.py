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


def get_recipe(recipes, name, amount_needed, leftovers):
    total = 0
    recipe = recipes[name]

    for ingredient in recipe.ingredients:
        if ingredient.name in recipes:  # Not ORE
            cost = get_recipe(recipes, ingredient.name, ingredient.amount, leftovers)
            total += cost
        else:
            total += ingredient.amount

    if name in leftovers:
        if leftovers[name] > amount_needed:
            leftovers[name] -= amount_needed
            return 0
        else:
            amount_needed -= leftovers[name]
            leftovers[name] = 0
    else:
        leftovers[name] = 0

    quantity_needed = math.ceil(amount_needed / recipe.output)
    leftovers[name] += (recipe.output * quantity_needed) - amount_needed

    return total * quantity_needed


def main():
    f = open("input-test.txt", "r")
    content = f.read()

    recipes = load_recipes(content)

    print(get_recipe(recipes, 'FUEL', 1, {}))


if __name__ == "__main__":
    main()
