import io
from unittest import TestCase
from unittest.mock import patch
from game import attack_foe as attack


class TestAttackFoe(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_foe_attack_once(self, mock_output):
        player = {'Current HP': 10, 'Level': 1, 'Attack': 3, 'Attack description': 'You glared menacingly', 'EXP': 50,
                  'Number of Attacks': 1, 'Name': 'Cindy'}
        enemy = {'Name': 'anti-masker', 'Current HP': 5, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1,
                 'Attack description': 'refuse to wash its hands too!'}
        expected = """
Cindy You glared menacingly It Inflicts 3 damage to anti-masker.
anti-masker has 2 HP.
"""
        attack(player, enemy)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_attack_character(self, mock_output):
        enemy = {'Current HP': 20, 'Level': 1, 'Attack': 5, 'Attack description': 'You glared menacingly',
                 'EXP': 50,
                 'Number of Attacks': 1, 'Name': 'Cindy'}
        player = {'Name': 'anti-masker', 'Current HP': 5, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1,
                  'Attack description': 'refuse to wash its hands too!'}
        expected = """
Cindy You glared menacingly It Inflicts 5 damage to anti-masker.
anti-masker has 0 HP.
"""
        attack(enemy, player)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_foe_attack_twice(self, mock_output):
        player = {'Current HP': 10, 'Level': 1, 'Attack': 3, 'Attack description': 'You glared menacingly',
                  'EXP': 50,
                  'Number of Attacks': 2, 'Name': 'Cindy'}
        enemy = {'Name': 'anti-masker', 'Current HP': 15, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1,
                 'Attack description': 'refuse to wash its hands too!'}
        expected = """
Cindy You glared menacingly It Inflicts 3 damage to anti-masker.
anti-masker has 12 HP.

Cindy You glared menacingly It Inflicts 3 damage to anti-masker.
anti-masker has 9 HP.
"""
        attack(player, enemy)
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_attack_foe_until_negative_HP(self, mock_output):
        player = {'Current HP': 10, 'Level': 1, 'Attack': 10, 'Attack description': 'You glared menacingly', 'EXP': 50,
                  'Number of Attacks': 1, 'Name': 'Cindy'}
        enemy = {'Name': 'anti-masker', 'Current HP': 5, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1,
                 'Attack description': 'refuse to wash its hands too!'}
        expected = """
Cindy You glared menacingly It Inflicts 10 damage to anti-masker.
anti-masker has -5 HP.
"""
        attack(player, enemy)
        self.assertEqual(mock_output.getvalue(), expected)
