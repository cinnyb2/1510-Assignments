from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes as foe_checker


class TestCheckForFor(TestCase):

    @patch('random.randint', return_value=0)
    def test_check_for_foes_foe_present(self, _):
        expected = True
        actual = foe_checker()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_check_for_foes_no_foes(self, _):
        expected = False
        actual = foe_checker()
        self.assertEqual(expected, actual)
