from unittest import TestCase
import list_manipulator as lm

class TestListManipulator(TestCase):
    def test_it_returns_the_elements_at_odd_positions(self):
        l = lm.odd_elements(["a", "b", "c", "d", "r", "t"])

        self.assertEqual(l, ["b", "d", "t"])

    def test_it_combine_two_lists_alternatingly(self):
        l = lm.combine(["a", "b", "c"], [1, 2, 3])

        self.assertEqual(l, ["a", 1, "b", 2, "c", 3])
