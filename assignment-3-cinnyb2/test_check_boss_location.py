from unittest import TestCase
from game import check_boss_location as check_boss_location


class TestCheckBossLocation(TestCase):
    def test_both_character_and_boss_in_same_location(self):
        player = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 5}
        boss = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 20}
        expected = check_boss_location(player, boss)
        actual = True
        self.assertEqual(expected, actual)

    def test_character_and_boss_not_in_same_location(self):
        player = {'X-coordinate': 20, 'Y-coordinate': 19, 'Current HP': 5}
        boss = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 20}
        expected = check_boss_location(player, boss)
        actual = False
        self.assertEqual(expected, actual)
