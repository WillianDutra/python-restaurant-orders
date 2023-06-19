from models.ingredient import Ingredient  # noqa: F401, E261, E501
from models.dish import Dish  # noqa: F401, E261, E501


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, 'r') as file:
            data = file.readlines()

            new_dish = None
            for line in range(1, len(data)):
                line_data = data[line].split(',')
                previos_line_data = data[line - 1].split(',')

                if line_data[0] != previos_line_data[0] or new_dish is None:
                    if new_dish is not None:
                        self.dishes.add(new_dish)
                    new_dish = Dish(line_data[0], float(line_data[1]))

                quantity = line_data[3].rstrip('\n')
                ingredient = Ingredient(line_data[2])
                new_dish.add_ingredient_dependency(ingredient, int(quantity))

                if line == len(data) - 1:
                    self.dishes.add(new_dish)
