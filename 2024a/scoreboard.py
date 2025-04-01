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
2. This question involves a scoreboard for a game. The game is played between two teams who alternate turns so
that at any given time, one team is active and the other team is inactive. During a turn, a team makes one or
more plays. Each play can score one or more points and the team’s turn continues, or the play can fail, in
which case no points are scored and the team’s turn ends. The Scoreboard class, which you will write, is
used to keep track of the score in a game.

    The Scoreboard class contains a constructor and two methods.

    • The constructor has two parameters. The first parameter is a String containing the
    name of team 1, and the second parameter is a String containing the name of team 2.
    The game always begins with team 1 as the active team.

    • The recordPlay method has a single nonnegative integer parameter that is equal to the
    number of points scored on a play or 0 if the play failed. If the play results in one or
    more points scored, the active team’s score is updated and that team remains active. If the
    value of the parameter is 0, the active team’s turn ends and the inactive team becomes the
    active team. The recordPlay method does not return a value.

    • The getScore method has no parameters. The method returns a String containing
    information about the current state of the game. The returned string begins with the score of
    team 1, followed by a hyphen ("-"), followed by the score of team 2, followed by a
    hyphen, followed by the name of the team that is currently active.
"""

import random
import math

class Scoreboard():

    def __init__(ARGS_GO_HERE):
        """
        • The constructor has two parameters. The first parameter (asides from self) is a String containing the
        name of team 1, and the second parameter is a String containing the name of team 2.
        The game always begins with team 1 as the active team.
        """
        pass

    def recordPlay(ARGS_GO_HERE):
        """
        • The recordPlay method has a single nonnegative integer parameter that is equal to the
        number of points scored on a play or 0 if the play failed. If the play results in one or
        more points scored, the active team’s score is updated and that team remains active. If the
        value of the parameter is 0, the active team’s turn ends and the inactive team becomes the
        active team. The recordPlay method does not return a value.
        """
        pass

    def getScore(ARGS_GO_HERE):
        """
        • The getScore method has no parameters. The method returns a String containing
        information about the current state of the game. The returned string begins with the score of
        team 1, followed by a hyphen ("-"), followed by the score of team 2, followed by a
        hyphen, followed by the name of the team that is currently active.
        """
        pass


"""
***DO NOT TOUCH ANY CODE BELOW***

STUFF BELOW IS UNIT TEST TO VERIFY FUNCTIONALITY OF CODE UNDER DIFFERENT SCENARIOS
"""

import unittest

class TestScoreboarrd(unittest.TestCase):

    def testNewGame(self):
        """unit test for creation of new game and verifying default score at start
        """
        info:str = ""
        game:Scoreboard = Scoreboard("Red", "Blue")

        info = game.getScore()

        self.assertEqual(info, "0-0-Red", "Score is wrong.")

    def testFirstTeamScores(self):

        info:str = ""
        game:Scoreboard = Scoreboard("Red", "Blue")

        info = game.getScore()
      
        game.recordPlay(1)
        game.recordPlay(2)
        game.recordPlay(3)

        self.assertEqual(info, "6-0-Red", "Score is wrong.")

    def testTeamSwitchScores(self):
        
        info:str = ""
        game:Scoreboard = Scoreboard("Red", "Blue")

        info = game.getScore()
      
        game.recordPlay(1)
        game.recordPlay(2)
        game.recordPlay(3)
        game.recordPlay(0)

        self.assertEqual(info, "6-0-Blue", "Score is wrong.")



    def testFullSequence(self):
        """unit test for full game sequence
        """

        info:str = ""

        #game is a new Scoreboard for a game played between team 1,
        #   whose name is "Red", and team 2, whose name is "Blue". 
        #   The active team is set to team 1.
        game:Scoreboard = Scoreboard("Red", "Blue")

        #expected value: "0-0-Red"
        info = game.getScore()

        #Team 1 earns 1 point because the game always begins with team 1 as the active team.
        game.recordPlay(1)

        #expected value: "1-0-Red"
        info = game.getScore(); 

        #Team 1’s play failed, so team 2 is now active.
        game.recordPlay(0)

        #expected value is "1-0-Blue"
        info = game.getScore()

        #expected value is "1-0-Blue"
        #The score and state of the game are unchanged since the last call to getScore
        info = game.getScore()

        #Team 2 earns 3 points.
        game.recordPlay(3)

        #expected value: "1-3-Blue"
        info = game.getScore()

        #Team 2 earns 1 point.
        game.recordPlay(1)

        #Team 2’s play failed, so team 1 is now active.
        game.recordPlay(0); 

        #expected value: "1-4-Red"
        info = game.getScore()

        #Team 1’s play failed, so team 2 is now active.
        game.recordPlay(0)

        #Team 2 earns 4 points.
        game.recordPlay(4)

        #Team 2’s play failed, so team 1 is now active.
        game.recordPlay(0)

        #expected value: "1-8-Red"
        info = game.getScore()

        #match is a new and independent Scoreboard object
        match:Scoreboard = Scoreboard("Lions", "Tigers")

        #expected value: "1-8-Red"
        info = game.getScore()

        self.assertEqual(info, "1-8-Red", "Score is wrong.")

if __name__ == '__main__':
    unittest.main()
