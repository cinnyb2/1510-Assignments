from unittest import TestCase
from game import level_checker as level_checker


class TestLevelChecker(TestCase):
    def test_level_checker_EXP_reached_for_level_3(self):
        player = {'EXP': 200}
        expected = level_checker(player)
        actual = True
        self.assertEqual(expected, actual)

    def test_level_checker_EXP_reached_for_level_2(self):
        player = {'EXP': 100}
        expected = level_checker(player)
        actual = True
        self.assertEqual(expected, actual)

    def test_level_checker_EXP_not_reached_within_level_defined(self):
        player = {'EXP': 101}
        expected = level_checker(player)
        actual = False
        self.assertEqual(expected, actual)

    def test_level_checker_EXP_not_reached_and_beyond_level_defined(self):
        player = {'EXP': 1000000}
        expected = level_checker(player)
        actual = False
        self.assertEqual(expected, actual)
