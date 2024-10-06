import unittest
from pg.tools import *


class TestSum(unittest.TestCase):

    def test_plate_format_to_random_00(self):
        r = plate_format_to_random(plate_format='ABC-123', text_set='ABCDEF', number_min=0, number_max=999)
        ground = {'a':1}
        self.assertEqual(r, None, "Should be 0, 0")


if __name__ == '__main__':
    unittest.main()
