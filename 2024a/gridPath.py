"""
Source:
    https://apcentral.collegeboard.org/media/pdf/ap24-frq-comp-sci-a.pdf

• Assume that built-in Python libraries (like random, math, os, etc.) have been imported where appropriate.
• Unless otherwise noted in the question, assume that parameters in method calls are not null and that methods
are called only when their preconditions are satisfied.
• In writing solutions for each question, you may use any of the accessible methods that are listed in classes defined
in that question. Writing significant amounts of code that can be replaced by a call to one of these methods will not
receive full credit.
"""

"""
4. This question involves a path through a two-dimensional (2D) array of integers, where the path is based on the
    values of elements in the array. 
    
    The grid starts from the top left at (0, 0)

    When an element of the 2D array is accessed, the first index is used to specify
    the row and the second index is used to specify the column. 
    
    The following Location class represents a row and column position in the 2D array.

    NOTE: Check the prompt for Problem 4 to see illustrations
"""

#DO NOT MAKE ANY CHANGES TO THE Location CLASS OR ANY OF ITS FUNCTIONS/METHODDS
class Location():

    def __init__(self, row, col):

        self.theRow = row
        self.theCol = col
    
    def getRow(self):
        return self.theRow
    
    def getCol(self):
        return self.theCol
    
class GridPath():

    def __init__(self, grid:list[list[int]]):
        """
        self.grid shall be a 2-d matrix of integers
        """
        
        self.grid = grid

    def getNextLoc(self, row:int, col:int) -> Location:
        """
        * Returns the Location representing a neighbor of the grid element at row and col,
        * as described in part (a)
        * Preconditions: row is a valid row index and col is a valid column index in grid.
        * row and col do not specify the element in the last row and last column of grid.

        Note: Refer to 4a in the PDF for illustrated examples

        Write the getNextLoc method, which returns a Location object that represents the smaller of
            two neighbors of the grid element at row and col, according to the following rules.

            • The two neighbors that are considered are the element below the given element and the
            element to the right of the given element, if they exist.
            
            • If both neighbors exist, the Location of the neighbor with the smaller value is
            returned. Two neighbors will always have different values.
            
            • If only one neighbor exists, the Location of the existing neighbor is returned.
        """
        
        return
    
    def sumPath(self, row:int, col:int) -> int:
        """
        * Computes and returns the sum of all values on a path through grid, as described in part (b)
        * Preconditions: row is a valid row index and col is a valid column index in grid.
        * row and col do not specify the element in the last row and last column of grid.

        Write the sumPath method, which returns the sum of all values on a path in grid. The path
        begins with the element at row and col and is determined by successive calls to getNextLoc.
        The path ends when the element in the last row and the last column of grid is reached.

        """

        return


"""
***DO NOT TOUCH ANY CODE BELOW***

STUFF BELOW IS UNIT TEST TO VERIFY FUNCTIONALITY OF CODE UNDER DIFFERENT SCENARIOS
"""

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
