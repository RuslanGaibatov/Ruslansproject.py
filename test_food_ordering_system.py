import unittest
from food_ordering_system import FoodOrderingSystem

class TestFoodOrderingSystem(unittest.TestCase):
    def setUp(self):
        self.food_ordering_system = FoodOrderingSystem()

    def test_add_item_to_menu(self):
        self.food_ordering_system.add_item_to_menu("Піца", "Піци", 12.99)
        self.assertIn({'name': "Піца", 'category': "Піци", 'price': 12.99}, self.food_ordering_system.menu)

if __name__ == '__main__':
    unittest.main()
