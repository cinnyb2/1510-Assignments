import io
from unittest import TestCase
from game import choose_character as character
from unittest.mock import patch


class TestChooseCharacter(TestCase):
    @patch('builtins.input', side_effect=['cindy', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_character_vulnerable_senior(self, _, __):
        expected_output = {'X-coordinate': 20, 'Y-coordinate': 17, 'Current HP': 3, 'Level': 1,
                           'EXP': 0, 'Name': 'Cindy', 'Attack': 10, 'Number of Attacks': 1,
                           'Attack description': 'You showed your hospital bill.',
                           'Description': 'You don\'t have a lot of life you but you '
                                          'keep hanging on!'}
        actual_output = character()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['cindy', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_character_unemployed_new_grad(self, _, __):
        expected_output = {'X-coordinate': 5, 'Y-coordinate': 2, 'Current HP': 8,
                           'Level': 1, 'EXP': 0, 'Name': 'Cindy', 'Attack': 5,
                           'Number of Attacks': 1,
                           'Attack description': 'You threw your overpriced textbook.',
                           'Description': 'You are hopeful but a bit jaded.'}
        actual_output = character()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['cindy', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_character_furloughed_worker(self, _, __):
        expected_output = {'X-coordinate': 8, 'Y-coordinate': 7, 'Current HP': 15, 'Level': 1,
                           'Description': 'You are just done with life.', 'Name': 'Cindy',
                           'Attack': 2, 'EXP': 0, 'Number of Attacks': 1,
                           'Attack description': 'You showed your receding hairline.'}
        actual_output = character()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['cindy', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_character_angry_teenager(self, _, __):
        expected_output = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Level': 1,
                           'Description': 'You don\'t know why but you are angry at everything.',
                           'Name': 'Cindy', 'Attack': 8, 'EXP': 0, 'Number of Attacks': 1,
                           'Attack description': 'You told the foe that you just don\'t want to '
                                                 'talk about it.'}
        actual_output = character()
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['cindy', '5', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_character_input_space(self, mock_output, _):
        expected_return = character()
        actual = mock_output.getvalue()
        expected = "That is an invalid answer. Please choose again (1, 2, 3, 4): "
        self.assertTrue(expected in actual)
        self.assertEqual({'Attack': 10,
                          'Attack description': 'You showed your hospital bill.',
                          'Current HP': 3,
                          'Description': "You don't have a lot of life you but you keep hanging on!",
                          'EXP': 0,
                          'Level': 1,
                          'Name': 'Cindy',
                          'Number of Attacks': 1,
                          'X-coordinate': 20,
                          'Y-coordinate': 17}, expected_return)
