import unittest
from app.funtion.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # setup
        cal = Calculator()
        expected_result = 10

        # action
        action_result = cal.add(2,3,5)

        # assert
        self.assertEqual(expected_result, action_result)

