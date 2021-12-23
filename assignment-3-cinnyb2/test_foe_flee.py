from unittest import TestCase
from unittest.mock import patch
from game import foe_flee as foe_flee


class TestCheckForFor(TestCase):

    @patch('random.randint', return_value=0)
    def test_foe_flee(self, _):
        expected = True
        actual = foe_flee()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_foe_stay_one(self, _):
        expected = False
        actual = foe_flee()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_foes_stay_two(self, _):
        expected = False
        actual = foe_flee()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_foes_stay_three(self, _):
        expected = False
        actual = foe_flee()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_foes_stay_four(self, _):
        expected = False
        actual = foe_flee()
        self.assertEqual(expected, actual)
