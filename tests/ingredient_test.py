from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as ingredient_types
import pytest

class TestIngredient:
    def test_create_ingredient(self):
        name = "name"
        price = 123.45
        type = ingredient_types.INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(type, name, price)

        assert ingredient.name == name
        assert ingredient.price == price
        assert ingredient.type == type

    def test_get_name(self):
        name = "name"
        price = 123.45
        type = ingredient_types.INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_name() == name

    def test_get_price(self):
        name = "name"
        price = 123.45
        type = ingredient_types.INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
            "ingredient_type",
            [ingredient_types.INGREDIENT_TYPE_FILLING, ingredient_types.INGREDIENT_TYPE_SAUCE]
    )
    def test_get_type(self, ingredient_type):
        name = "name"
        price = 123.45
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type