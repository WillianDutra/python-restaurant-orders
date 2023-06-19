from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest

# Req 2
def test_dish():
    dish_1 = Dish("Spaghetti", 10.50)
    dish_2 = Dish("Spaghetti", 10.50)
    dish_3 = Dish("Arroz Carreteiro", 12.50)
    
    # name/price/repr
    assert dish_1.name == "Spaghetti"
    assert dish_1.price == 10.5
    assert repr(dish_1) == "Dish('Spaghetti', R$10.50)"
    
    # hash
    assert hash(dish_1) == hash(dish_2)
    assert hash(dish_1) != hash(dish_3)

    # eq
    assert dish_1 == dish_2
    assert (dish_1 == dish_3) == False

    # ingredients
    dish_1.add_ingredient_dependency("Macarrão", 10)
    assert dish_1.get_ingredients() == {"Macarrão"}
    assert dish_1.get_restrictions() == set()

    # errors
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Spaghettti", "1")

    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        Dish("Spaghetti", 0)
