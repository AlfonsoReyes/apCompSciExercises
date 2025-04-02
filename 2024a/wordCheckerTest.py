"""
***DO NOT TOUCH ANY CODE BELOW***

STUFF BELOW IS UNIT TEST TO VERIFY FUNCTIONALITY OF CODE UNDER DIFFERENT SCENARIOS
"""

from wordChecker import WorkChecker
import unittest

class TestWorkChecker(unittest.TestCase):

    def testIsWordChainOne(self):

        wc = WorkChecker(["an", "band", "band","abandon"])

        result = wc.isWordChain()
        
        self.assertEqual(result, True, "Invalid isWordChain() result.")

    def testIsWordChainTwo(self):

        wc = WorkChecker(["to", "too", "stool","tools"])

        result = wc.isWordChain()
        
        self.assertEqual(result, False, "Invalid isWordChain() result.")

    def testCreateListOne(self):

        wc = WorkChecker(["catch", "bobcat", "catchacat", "cat", "at"])

        result = wc.createList("cat")

        self.assertEqual(result, ["ch", "chacat", ""], "Invalid result list.")        

    def testCreateListTwo(self):

        wc = WorkChecker(["catch", "bobcat", "catchacat", "cat", "at"])

        result = wc.createList("catch")

        self.assertEqual(result, ["", "acat"], "Invalid result list.")        

    def testCreateListThree(self):

        wc = WorkChecker(["catch", "bobcat", "catchacat", "cat", "at"])

        result = wc.createList("dog")

        self.assertEqual(result, [], "Invalid result list.")        

if __name__ == '__main__':
    unittest.main()
