from unittest import TestCase
from unittest.mock import patch
from game import foe_generator as foe_generator


class TestFoeGenerator(TestCase):
    def test_foe_generator_data_type(self):
        self.assertIsInstance(foe_generator(), dict)

    @patch('random.choice', return_value='online learning')
    def test_foe_generator_with_one_of_options_listed(self, _):
        expected = {'Attack': 1,
                    'Attack description': 'Its trying its best to make you miserable.',
                    'Current HP': 5,
                    'EXP': 50,
                    'Name': 'online learning',
                    'Number of Attacks': 1}
        actual = foe_generator()
        self.assertEqual(expected, actual)
