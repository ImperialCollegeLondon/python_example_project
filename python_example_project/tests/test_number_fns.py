import unittest

from python_example_project.number_fns import square, cube

unittest.main(argv=['first-arg-is-ignored'], exit=False)


class test_square(unittest.TestCase):

    def test_float(self):
        self.assertEqual(square(2.), 4.)
        self.assertEqual(cube(2.), 8.)

    def test_int(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(cube(2), 8)

