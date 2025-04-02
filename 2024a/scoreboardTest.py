"""
***DO NOT TOUCH ANY CODE BELOW***

STUFF BELOW IS UNIT TEST TO VERIFY FUNCTIONALITY OF CODE UNDER DIFFERENT SCENARIOS
"""

from scoreboard import Scoreboard
import unittest

class TestScoreboard(unittest.TestCase):

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
