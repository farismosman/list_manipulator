from unittest import TestCase
import list_manipulator as lm

class TestListManipulator(TestCase):
    def test_it_returns_the_elements_at_odd_positions(self):
        l = lm.odd_elements(["a", "b", "c", "d", "r", "t"])

        self.assertEqual(l, ["b", "d", "t"])
