from unittest import TestCase
from game import check_if_goal_attained as goal_checker


class TestCheckIfGoalAttained(TestCase):
    def test_goal_attained(self):
        board = {(0, 0): 'room 1', (1, 0): 'room 2', (20, 20): 'room 3'}
        character = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 5}
        boss = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 0, 'Attack': 2}
        expected = True
        actual = goal_checker(board, character, boss)
        self.assertEqual(expected, actual)

    def test_goal_not_attained(self):
        board = {(0, 0): 'room 1', (2, 0): 'room 2', (20, 20): 'room 3'}
        character = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 0}
        boss = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 13, 'Attack': 2}
        expected = False
        actual = goal_checker(board, character, boss)
        self.assertEqual(expected, actual)

    def test_goal_attained_but_both_game_boss_and_character_dies(self):
        board = {(0, 0): 'room 1', (2, 0): 'room 2', (20, 20): 'room 3'}
        character = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 0}
        boss = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 0, 'Attack': 2}
        expected = True
        actual = goal_checker(board, character, boss)
        self.assertEqual(expected, actual)
