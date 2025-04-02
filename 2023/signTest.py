"""
***DO NOT ALTER ANY CODE BELOW***

CODE BELOW IS FOR UNIT TESTING FUNCTIONALITY OF Sign CLASS UNDER DIFFERENT SCENARIOS
"""

from sign import Sign
import unittest
import random
import math


class SignTest(unittest.TestCase):

    def testOne(self):

        s = None    #output of getLines method
        x = None    #output of numberOfLines method

        sign = Sign("ABC222DE", 3)

        x = sign.numberOfLines()
        s = sign.getLines()

        self.assertEqual((x, s), (3, "ABC;222;DE"), "Invalid output for numberOfLines or getLines methods.")

    def testTwo(self):

        s = None    #output of getLines method
        x = None    #output of numberOfLines method

        sign = Sign("ABCD", 10)

        x = sign.numberOfLines()
        s = sign.getLines()

        self.assertEqual((x, s), (1, "ABCD"), "Invalid output for numberOfLines or getLines methods.")

    def testThree(self):

        s = None    #output of getLines method
        x = None    #output of numberOfLines method

        sign = Sign("ABCDEF", 6)

        x = sign.numberOfLines()
        s = sign.getLines()

        self.assertEqual((x, s), (1, "ABCDEF"), "Invalid output for numberOfLines or getLines methods.")

    def testFour(self):

        s = None    #output of getLines method
        x = None    #output of numberOfLines method

        sign = Sign("AB_CD_EF", 2)

        x = sign.numberOfLines()
        s = sign.getLines()

        self.assertEqual((x, s), (4, "AB;_C;D_;EF"), "Invalid output for numberOfLines or getLines methods.")

    def testFive(self):

        s = None    #output of getLines method
        x = None    #output of numberOfLines method

        sign = Sign("", 4)

        x = sign.numberOfLines()
        s = sign.getLines()

        self.assertEqual((x, s), (0, None), "Invalid output for numberOfLines or getLines methods.")

if __name__ == '__main__':
    unittest.main()

