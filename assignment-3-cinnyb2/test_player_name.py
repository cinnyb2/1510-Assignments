from unittest import TestCase
from game import player_name as name
from unittest.mock import patch


class TestPlayName(TestCase):
    @patch('builtins.input', side_effect=['cindy'])
    def test_player_name_letters_lowercase(self, _):
        expected = 'Cindy'
        actual = name()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['CINDY'])
    def test_player_name_letters_uppercase(self, _):
        expected = 'Cindy'
        actual = name()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=[' '])
    def test_player_name_space(self, _):
        expected = ' '
        actual = name()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['dh2pf'])
    def test_player_name_letters_and_numbers(self, _):
        expected = 'Dh2Pf'
        actual = name()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['16954360'])
    def test_player_name_numbers(self, _):
        expected = '16954360'
        actual = name()
        self.assertIn(expected, actual)
