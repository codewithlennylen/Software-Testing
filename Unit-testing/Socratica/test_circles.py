import unittest
from circles import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2) # Checks for consistency up-to 7 d.p.

    def test_value(self):
        # Make sure the function raises errors where necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure the function raises type-errors where necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
