from proj.inventory import MobileInventoty,InsufficientException
import pytest
class TestingInventoryCreation:
    def test_creating_empty_inventory(self):
        m=MobileInventoty(None)
        assert m.balance_inventory == {}
    def test_creating_specified_inventory(self):
        m1=MobileInventoty({'IPhone Model X':100,'Xiaomi Model Y':1000,'Nokia Model Z':25})
        assert m1.balance_inventory["IPhone Model X"] == 100
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError):
            m2=MobileInventoty(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError):
            m3=MobileInventoty({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError):
            m4=MobileInventoty({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'})
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError):
            m5=MobileInventoty({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25})

class TestInventoryAddStock:
    @classmethod
    def setup_class(cls):
        cls.inventory = MobileInventoty({'iPhone Model X': 100, 'Xiaomi Model Y': 1000, 'Nokia Model Z': 25})

    def test_add_new_stock_as_dict(self):
        self.inventory.add_stock({'iPhone Model X': 50, 'Xiaomi Model Y': 2000, 'Nokia Model A': 10})
        assert self.inventory.balance_inventory == {'iPhone Model X': 150, 'Xiaomi Model Y': 3000, 'Nokia Model Z': 25,
                                                    'Nokia Model A': 10}

    def test_add_new_stock_as_list(self):

        with pytest.raises(TypeError):
            self.inventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])

    def test_add_new_stock_with_numeric_keys(self):
        d = {1: 'iPhone Model A', 2: 'Xiaomi Model B', 3: 'Nokia Model C'}
        with pytest.raises(ValueError):
            self.inventory.add_stock(d)

    def test_add_new_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError):
            self.inventory.add_stock({'iPhone Model A': '50', 'Xiaomi Model B': '2000', 'Nokia ModelC': '25'})

    def test_add_new_stock_with_float_values(self):
        with pytest.raises(ValueError):
            self.inventory.add_stock({'iPhone Model A': 50.5, 'Xiaomi Model B': 2000.3, 'Nokia Model C': 25})

class TestInventorySellStock():
    @classmethod
    def setup_class(cls):
        cls.inventory = MobileInventoty(
            {'iPhone Model A': 50, 'Xiaomi Model B': 2000, 'Nokia Model C': 10, 'Sony Model D': 1})

    def test_sell_stock_as_dict(self):
        self.inventory.sell_stock({'iPhone Model A': 2, 'Xiaomi Model B': 20, 'Sony Model D': 1})
        assert self.inventory.balance_inventory == {'iPhone Model A': 48, 'Xiaomi Model B': 1980, 'Nokia Model C': 10,
                                                    'Sony Model D': 0}

    def test_sell_stock_as_list(self):
        with pytest.raises(TypeError):
            self.inventory.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])

    def test_sell_stock_with_numeric_keys(self):
        with pytest.raises(ValueError):
            self.inventory.sell_stock({1: 'iPhone Model A', 2: 'Xiaomi Model B', 3: 'Nokia Model C'})

    def test_sell_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError):
            self.inventory.sell_stock({'iPhone Model A': '5', 'Xiaomi Model B': '3', 'Nokia Model C': '4'})

    def test_sell_stock_with_float_values(self):
        with pytest.raises(ValueError):
            self.inventory.sell_stock({'iPhone Model A': 2.5, 'Xiaomi Model B': 3.1, 'Nokia Model C': 4})

    def test_sell_stock_of_nonexisting_model(self):
        with pytest.raises(InsufficientException):
            self.inventory.sell_stock({'iPhone Model B': 2, 'Xiaomi Model B': 5})

    def test_sell_stock_of_insufficient_stock(self):
        with pytest.raises(InsufficientException):
            self.inventory.sell_stock({'iPhone Model A': 2, 'Xiaomi Model B': 5, 'Nokia Model C': 15})


