from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("Macarrão")
    ingredient_2 = Ingredient("Macarrão")
    ingredient_3 = Ingredient("manteiga")

    # name
    assert ingredient_1.name == "Macarrão"

    # hash
    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)

    # eq
    assert ingredient_1 == ingredient_2
    assert (ingredient_1 == ingredient_3) == False

    # repr
    assert repr(ingredient_1) == "Ingredient('Macarrão')"

    # restrictionMap
    assert ingredient_1.restrictions == set()