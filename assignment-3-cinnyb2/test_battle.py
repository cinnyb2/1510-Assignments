import io
from unittest import TestCase
from game import battle as battle
from unittest.mock import patch


class TestBattle(TestCase):

    @patch('builtins.input', side_effect=['Attack'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle(self, mock_output, _):
        player = {'Current HP': 15, 'Level': 1, 'Attack': 10, 'Attack description': 'You glared menacingly', 'EXP': 50,
                  'Number of Attacks': 1, 'Name': 'Cindy'}
        enemy = {'Name': 'anti-masker', 'Current HP': 5, 'Attack': 1, 'EXP': 50, 'Number of Attacks': 1,
                 'Attack description': 'refuse to wash its hands too!'}
        battle(player, enemy)
        game_print = mock_output.getvalue()
        expected_output = '1. Attack \n2. Flee ' \
                          '\nPlease enter the number that correspond to the action you wish to take (1, 2): ' \
                          '\n\nCindy You glared menacingly It Inflicts 10 damage to anti-masker.' \
                          '\nanti-masker has -5 HP.\n\nYou have defeated anti-masker. You have gained 100 EXP!\n'
        self.assertIn(expected_output, game_print)
