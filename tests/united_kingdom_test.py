import unittest
from pg.united_kingdom import *


class TestSum(unittest.TestCase):

    def test_point2d_frame_to_point2d_real_00(self):
        r = vrpg_uk(font=None, dir='d:/temp/img/')
        ground = {'a':1}
        self.assertEqual(r, None, "Should be 0, 0")


if __name__ == '__main__':
    unittest.main()
