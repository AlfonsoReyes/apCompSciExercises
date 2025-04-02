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


