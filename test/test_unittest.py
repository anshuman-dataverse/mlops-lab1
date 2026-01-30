import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculator import fun1, fun2, fun3, fun4

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)
        self.assertEqual(fun1(-1, 1), 0)
        self.assertEqual(fun1(0, 0), 0)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)
        self.assertEqual(fun2(10, 5), 5)
        self.assertEqual(fun2(3, 3), 0)

    def test_fun3(self):
        self.assertEqual(fun3(2, 3), 6)
        self.assertEqual(fun3(4, 5), 20)
        self.assertEqual(fun3(0, 10), 0)

    def test_fun4(self):
        self.assertEqual(fun4(2, 3), 10)
        self.assertEqual(fun4(5, 5), 35)

if __name__ == '__main__':
    unittest.main()
