from unittest import TestCase
from unittest.mock import patch
from game import generate_random_tile_description


class TestGenerateRandomTileDescription(TestCase):

    @patch('random.randint', return_value=0)
    def test_generate_random_tile_description_first_index_item(self, _):
        actual = generate_random_tile_description()
        expected = 'You see nothing, the emptiness fills you with dread.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_generate_random_tile_description_second_index_item(self, _):
        actual = generate_random_tile_description()
        expected = 'You have entered a hallway full of monster statues, you are filled with fear.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_generate_random_tile_description_third_index_item(self, _):
        actual = generate_random_tile_description()
        expected = 'You see a small light, which sparks hope in you.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_generate_random_tile_description_forth_index_item(self, _):
        actual = generate_random_tile_description()
        expected = 'You have entered an abandoned room. The nauseating stench gives you a headache.'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_generate_random_tile_description_last_index_item(self, _):
        actual = generate_random_tile_description()
        expected = 'You are surrounded by tall grass.'
        self.assertEqual(expected, actual)
