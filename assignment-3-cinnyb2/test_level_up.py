from unittest import TestCase
from game import level_up as level_up


class TestLevelUp(TestCase):
    def test_level_up_to_three(self):
        player = {'Level': 2, 'EXP': 200, 'Current HP': 5, 'Attack': 2}
        expected = level_up(player)
        actual = {'Level': 3, 'EXP': 200, 'Current HP': 8, 'Attack': 9}
        self.assertEqual(expected, actual)

    def test_level_up_to_two(self):
        player = {'Level': 1, 'EXP': 100, 'Current HP': 5, 'Attack': 2}
        expected = level_up(player)
        actual = {'Level': 2, 'EXP': 100, 'Current HP': 7, 'Attack': 4}
        self.assertEqual(expected, actual)

    def test_not_enough_exp_to_level_up(self):
        player = {'Level': 1, 'EXP': 150, 'Current HP': 5, 'Attack': 2}
        expected = level_up(player)
        actual = {'Level': 1, 'EXP': 150, 'Current HP': 5, 'Attack': 2}
        self.assertEqual(expected, actual)

    def test_level_up_beyond_3(self):
        player = {'Level': 3, 'EXP': 200, 'Current HP': 8, 'Attack': 9}
        expected = level_up(player)
        actual = {'Level': 3, 'EXP': 200, 'Current HP': 8, 'Attack': 9}
        self.assertEqual(expected, actual)
