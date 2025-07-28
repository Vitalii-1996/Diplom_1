from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock, patch
import praktikum
import pytest

class TestBurger():
    def test_burger_init(self):
        burger = Burger()
        assert burger.bun == None
        assert burger.ingredients == []

    def test_burger_set_bun(self):
        bun_mock = Mock()
        burger = Burger()
        burger.set_buns(bun_mock)

        assert burger.bun == bun_mock

    @pytest.mark.parametrize(
            'indigrients,expected_len',
            [
                [[Mock()],1],
                [[Mock(), Mock()],2]
            ]
    )
    def test_append_indigrients(self, indigrients, expected_len):
        burger = Burger()
        for indigrient in indigrients:
            burger.add_ingredient(indigrient)
        assert len(burger.ingredients) == expected_len

    @pytest.mark.parametrize(
            'indigrients, index',
            [
                [[Mock(), Mock()],0],
                [[Mock(), Mock()],1]
            ]
    )
    def test_remove_indigrient(self,indigrients, index):
        burger = Burger()
        for indigrient in indigrients:
            burger.add_ingredient(indigrient)

        burger.remove_ingredient(index)

        assert len(burger.ingredients) == len(indigrients) - 1
        assert indigrients[index] not in burger.ingredients

    @pytest.mark.parametrize(
            'indigrients, index, new_index',
            [
                [[Mock(), Mock(), Mock()],0,2],
                [[Mock(), Mock(), Mock()],2,0]
            ]
    )
    def test_move_indigrient(self,indigrients, index, new_index):
        burger = Burger()
        for indigrient in indigrients:
            burger.add_ingredient(indigrient)

        burger.move_ingredient(index, new_index)
        
        assert indigrients[index] == burger.ingredients[new_index]

    @pytest.mark.parametrize(
            "bun, ingredients, expected_price",
            [
                [Bun('test',123), None, 200],
                [Bun('test',123), [Ingredient('test', 'test',123)], 300],
                [Bun('test',123), [Ingredient('test', 'test',123), Ingredient('test', 'test',123)], 400],
            ]
    )
    @patch('praktikum.ingredient.Ingredient.get_price', return_value = 100)
    @patch('praktikum.bun.Bun.get_price', return_value = 100)
    def test_get_burger_price(self, mock_bun_get_price, mock_ingredient_get_price, bun, ingredients, expected_price,):
        burger = Burger()
        if bun != None:
            burger.set_buns(bun)
        if ingredients != None:
            for indigrient in ingredients:
                burger.add_ingredient(indigrient)
        assert burger.get_price() == expected_price