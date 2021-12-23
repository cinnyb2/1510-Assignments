from unittest import TestCase
from game import make_boss as make_boss


class TestMakeBoss(TestCase):
    def test_make_boss(self):
        actual = make_boss()
        expected = {'X-coordinate': 20, 'Y-coordinate': 20, 'Current HP': 15, 'Attack': 2, 'EXP': 100000000,
                    'Description': 'Despite being a non-living object, it smirks at the thought of you fighting it, '
                    'as it flashes its namesake crowns at you.', 'Name': 'SARS‐CoV‐2', 'Number of Attacks': 2,
                    'Attack description': 'is trying to mutate itself to have your DNA.'}
        self.assertEqual(expected, actual)
