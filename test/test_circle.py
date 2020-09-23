from proj.circle import MobileInventoty,InsufficientException
import pytest
class TestingInventoryCreation:
    def __init__(self):
        pass
    def test_creating_empty_inventory(self):
        m=MobileInventoty({})
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

