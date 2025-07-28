from praktikum.bun import Bun

class TestBun:
    def test_create_bun(self):
        name = "name"
        price = 123.45
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price

    def test_get_name(self):
        name = "name"
        price = 123.45
        bun = Bun(name, price)

        assert bun.get_name() == "name"

    def test_get_price(self):
        name = "name"
        price = 123.45
        bun = Bun(name, price)

        assert bun.get_price() == 123.45