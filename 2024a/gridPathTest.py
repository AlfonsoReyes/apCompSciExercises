"""
***DO NOT TOUCH ANY CODE BELOW***

STUFF BELOW IS UNIT TEST TO VERIFY FUNCTIONALITY OF CODE UNDER DIFFERENT SCENARIOS
"""

from gridPath import GridPath, Location
import unittest

class TestGridPath(unittest.TestCase):

    def testGetNextLocOne(self):

        #grid = [[]]

        grid = [
            [12, 3, 4, 13, 5],
            [11, 21, 2, 14, 16],
            [7, 8, 9, 15, 0],
            [10, 17, 20, 19, 1],
            [18, 22, 30, 25, 6]
        ]
        
        gp = GridPath(grid)

        loc = gp.getNextLoc(0, 0)

        locCoords = (loc.getRow(), loc.getCol())

        self.assertEqual(locCoords, (0, 1), "Incorrect location.")

    def testGetNextLocTwo(self):

        #grid = [[]]

        grid = [
            [12, 3, 4, 13, 5],
            [11, 21, 2, 14, 16],
            [7, 8, 9, 15, 0],
            [10, 17, 20, 19, 1],
            [18, 22, 30, 25, 6]
        ]

        gp = GridPath(grid)

        loc = gp.getNextLoc(2, 4)

        locCoords = (loc.getRow(), loc.getCol())

        self.assertEqual(locCoords, (3, 4), "Incorrect location.")

    def testGetNextLocThree(self):

        grid = [
            [12, 3, 4, 13, 5],
            [11, 21, 2, 14, 16],
            [7, 8, 9, 15, 0],
            [10, 17, 20, 19, 1],
            [18, 22, 30, 25, 6]
        ]

        gp = GridPath(grid)

        loc = gp.getNextLoc(1, 3)

        locCoords = (loc.getRow(), loc.getCol())

        self.assertEqual(locCoords, (2, 3), "Incorrect location.")

    def testGetNextLocFour(self):

        grid = [
            [12, 3, 4, 13, 5],
            [11, 21, 2, 14, 16],
            [7, 8, 9, 15, 0],
            [10, 17, 20, 19, 1],
            [18, 22, 30, 25, 6]
        ]

        gp = GridPath(grid)

        loc = gp.getNextLoc(4, 3)

        locCoords = (loc.getRow(), loc.getCol())

        self.assertEqual(locCoords, (4, 4), "Incorrect location.")

if __name__ == '__main__':
    unittest.main()
