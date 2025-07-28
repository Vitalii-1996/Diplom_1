from praktikum.database import Database

class TestDatabase:
    def test_create_database(self):
        database = Database()

        assert database.buns != None
        assert database.ingredients != None

    def test_available_buns_returns_value(self):
        database = Database()

        assert database.available_buns() != None

    def test_available_ingredients_returns_value(self):
        database = Database()

        assert database.available_ingredients() != None
