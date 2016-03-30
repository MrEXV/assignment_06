import os
import sys
import unittest
import random
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        # A list comprehension to create 50 random points
        self.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]


    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        x, y = analytics.mean_center(self.points)
        self.assertEqual(x, 47.52)
        self.assertEqual(y, 45.14)

    def test_minimum_bounding_rectangle(self):
        mbr = analytics.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0,0,94,98])

    def test_mbr_area(self):
        mbr = [0,0,94,98]
        area = analytics.mbr_area(mbr)
        self.assertEqual(area, 9212)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = analytics.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)
