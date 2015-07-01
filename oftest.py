#
# coding:utf-8;

import unittest
from ofspace import *


class OFSpaceTests(unittest.TestCase):

    def test_point_equality(self):
        self.assertEqual(Point(3.0, 5.0, 7.0),
            Point(3.0, 5.0, 7.0),
            "incorrect result when comparing two Points by ==")
        self.assertNotEqual(Point(3.0, 5.0, 7.0),
            Point(1.0, 5.0, 7.0),
            "incorrect result (x) when comparing two points by !=")
        self.assertNotEqual(Point(3.0, 5.0, 7.0),
            Point(3.0, 1.0, 7.0),
            "incorrect result (y) when comparing two points by !=")
        self.assertNotEqual(Point(3.0, 5.0, 7.0),
            Point(3.0, 5.0, 1.0),
            "incorrect result (z) when comparing two points by !=")

    def test_point_addition(self):
        self.assertEqual(Point(4.0, 6.0, 8.0),
            Point(1.0, 1.0, 1.0) + Point(3.0, 5.0, 7.0),
            "incorrect result when adding two Points")
        self.assertEqual(Point(4.0, 6.0, 8.0),
            Point(3.0, 5.0, 7.0) + 1,
            "incorrect result when adding Point and number")

    def test_point_subtraction(self):
        self.assertEqual(Point(3.0, 5.0, 7.0),
            Point(4.0, 6.0, 8.0) - Point(1.0, 1.0, 1.0),
            "incorrect result when subtracting two Points")
        self.assertEqual(Point(3.0, 5.0, 7.0),
            Point(4.0, 6.0, 8.0) - 1,
            "incorrect result when subtracting Point and number")

    def test_point_multiplication(self):
        self.assertEqual(Point(6.0, 10.0, 14.0),
            Point(3.0, 5.0, 7.0) * 2.0,
            "incorrect result when multiplying Point by number")

    def test_point_division(self):
        self.assertEqual(Point(3.0, 5.0, 7.0),
            Point(6.0, 10.0, 14.0) / 2.0,
            "incorrect result when dividing Point by number")

    def test_point_abslen(self):
        self.assertEqual(Point(1.0, 1.0, 1.0).abs(),
            sqrt(3.0),
            "incorrect result when getting Point length (abs)")

    def test_point_keyaccess(self):
        p = Point(3.0, 5.0, 7.0)
        for key in "xXuUrR":
            self.assertEqual(p[key], 3.0,
                "incorrect result when accesing Point value by '{0}' key".format((key)))
        for key in "yYvVgG":
            self.assertEqual(p[key], 5.0,
                "incorrect result when accesing Point value by '{0}' key".format((key)))
        for key in "zZwWbB":
            self.assertEqual(p[key], 7.0,
                "incorrect result when accesing Point value by '{0}' key".format((key)))
        for key,val in zip([0, 1, 2],[3.0, 5.0, 7.0]):
            self.assertEqual(p[key], val,
                "incorrect result when accesing Point value by '{0}' key".format((key)))

    def test_pointlist_sort(self):
        lst = PointList()
        lst.append(Point())
        lst.append(Point(1.0))
        self.assertEqual(lst[0], Point(),
            "incorrect result before sorting PointList by X")
        lst.sort(0)
        self.assertEqual(lst[0], Point(1.0),
            "incorrect result when sorting PointList by X")
        lst = PointList()
        lst.append(Point(1.0))
        lst.append(Point(1.0, 1.0))
        lst.sort(1)
        self.assertEqual(lst[0], Point(1.0, 1.0),
            "incorrect result when sorting PointList by Y")
        lst = PointList()
        lst.append(Point(1.0, 1.0))
        lst.append(Point(1.0, 1.0, 1.0))
        lst.sort(2)
        self.assertEqual(lst[0], Point(1.0, 1.0, 1.0),
            "incorrect result when sorting PointList by Z")

    def test_line_equality(self):
        ln1 = Line(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
        ln2 = Line(Point(1.0, 1.0, 1.0), Point(0.0, 0.0, 0.0))
        self.assertEqual(ln1, ln2,
            "incorrect result when comparing (eq) two Line(s) probably sorting problem")
        ln1 = Line(Point(0.0, 0.0, 0.0), Point(1.0, 1.0, 1.0))
        ln2 = Line(Point(0.0, 0.0, 0.0), Point(2.0, 2.0, 2.0))
        self.assertNotEqual(ln1, ln2,
            "incorrect result when comparing (ne) two Line(s) probably sorting problem")

    def test_line_intersection(self):
        ln1 = Line(Point(1.0, 1.0, 0.0), Point(3.0, 3.0, 0.0))
        ln2 = Line(Point(1.0, 3.0, 0.0), Point(3.0, 1.0, 0.0))
        res = ln1 / ln2
        if res:
            self.assertEqual(res, Point(2.0, 2.0, 0.0),
                "incorrect result when intersecting two xy Line(s) res({0})".format((str(res))))
        else:
            self.assertEqual(True, False,
                "incorrect result when intersecting two xy Line(s) res(False)")
        ln1 = Line(Point(0.0, 0.0, 0.0), Point(3.0, 3.0, 3.0))
        ln2 = Line(Point(0.0, 3.0, 0.0), Point(3.0, 0.0, 3.0))
        res = ln1 / ln2
        if res:
            self.assertEqual(res, Point(1.5, 1.5, 1.5),
                "incorrect result when intersecting two xyz Line(s) res({0})".format((str(res))))
        else:
            self.assertEqual(True, False,
                "incorrect result when intersecting two xyz Line(s) res(False)")


def run():
    ofspacesuite = unittest.TestLoader().loadTestsFromTestCase(OFSpaceTests)
    alltests = unittest.TestSuite([ofspacesuite])
    unittest.TextTestRunner(verbosity=2).run(alltests)