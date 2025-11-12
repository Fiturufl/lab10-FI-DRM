#https://github.com/Fiturufl/lab10-FI-DRM.git
#Partner 1: Francisco Iturriaga
#Partner 2: David Reyes-Munoz

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, 4), 8)
        self.assertEqual(add(10, -4), 6)


    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(2,1), 1)
        self.assertEqual(sub(10,4), 6)
        self.assertEqual(sub(10, -1), 11)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 99), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(-4, 12), -3.0)
        self.assertAlmostEqual(div(0.5, 1.5), 3.0)



    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 6)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(8,2), 3)
        self.assertEqual(log(100,10), 2)
        self.assertEqual(log(81,3), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(2, 1)

    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(9), 3.0)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()