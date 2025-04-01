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
3. This question involves the manipulation and analysis of a list of words. The following WordChecker
    class contains a list of strings (list[str]) to be analyzed and methods that are used to perform the
    analysis. You will write two methods of the WordChecker class.

    HINT:
    You can find built-in functions for strings here: (You will likely have to pick and choose one of these!)
        https://www.w3schools.com/python/python_ref_string.asp

"""

class WorkChecker():

    def __init__(self, wordList:list[str]):
        
        self.wordList:list[str] = wordList

    def isWordChain(self) -> bool:
        """
        * Returns true if each element of wordList (except the first) contains the previous
        * element as a substring and returns false otherwise, as described in part (a)
        * Precondition: wordList contains at least two elements.
        * Postcondition: wordList is unchanged.
        """
        return

    def createList(self, target:str) -> list[str]:
        """
        * Returns an list of strings (list[str]) based on strings from wordList that start
        * with target, as described in part (b). Each element of the returned ArrayList has had
        * the initial occurrence of target removed.
        * Postconditions: wordList is unchanged.
        * Items appear in the returned list in the same order as they appear in wordList
        
        Consider an example where wordList contains the following strings.
        ["catch", "bobcat", "catchacat", "cat", "at"]
        
        createList("cat") returns ["ch", "chacat", ""]
            - Only "catch", "catchacat", and"cat" begin with "cat"
        
        createList("catch") returns ["", "acat"]
            - Only "catch" and "catchacat" begin with "catch"

        createList("dog") returns []
            - None of the words in wordList begin with "dog", so returr empty list.
        """
        return
    
"""
***DO NOT TOUCH ANY CODE BELOW***

STUFF BELOW IS UNIT TEST TO VERIFY FUNCTIONALITY OF CODE UNDER DIFFERENT SCENARIOS
"""

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
