from unittest import TestCase
from unittest.mock import patch
from game import flee as flee
import io


class TestFlee(TestCase):
    @patch('random.randint', return_value=1)
    def test_flee_safe(self, _):
        character = {'Current HP': 10}
        expected = {'Current HP': 10}
        self.assertEqual(expected, flee(character))

    @patch('random.randint', return_value=2)
    def test_flee_safe_two(self, _):
        character = {'Current HP': 10}
        expected = {'Current HP': 10}
        self.assertEqual(expected, flee(character))

    @patch('random.randint', return_value=3)
    def test_flee_safe_three(self, _):
        character = {'Current HP': 10}
        expected = {'Current HP': 10}
        self.assertEqual(expected, flee(character))

    @patch('random.randint', side_effect=[0, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_got_hurt_print(self, mock_output, _):
        character = {'Current HP': 10}
        flee(character)
        game_print = mock_output.getvalue()
        expected_output = 'The enemy attack you as you flee, you took 1.'
        self.assertIn(expected_output, game_print)

    @patch('random.randint', side_effect=[1, 0])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_safe_flee_print(self, mock_output, _):
        character = {'Current HP': 10}
        flee(character)
        game_print = mock_output.getvalue()
        expected_output = '\nYou got away safely!\n'
        self.assertIn(expected_output, game_print)
