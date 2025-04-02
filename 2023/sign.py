"""
Source:
    https://apcentral.collegeboard.org/media/pdf/ap23-frq-comp-sci-a.pdf

    • Assume that built-in Python libraries (like random, math, os, etc.) have been imported where appropriate.
    • Unless otherwise noted in the question, assume that parameters in method calls are not null and that methods
    are called only when their preconditions are satisfied.
    • In writing solutions for each question, you may use any of the accessible methods that are listed in classes defined
    in that question. Writing significant amounts of code that can be replaced by a call to one of these methods will not
    receive full credit.
"""

"""
2. This question involves methods that distribute text across lines of an electronic sign. The electronic sign and
the text to be displayed on it are represented by the Sign class. You will write the complete Sign class,
which contains a constructor and two methods.

The Sign class constructor has two parameters. The first parameter is a String that contains the
message to be displayed on the sign. The second parameter is an int that contains the width of each line of
the sign. The width is the positive maximum number of characters that can be displayed on a single line of the
sign.

A sign contains as many lines as are necessary to display the entire message. The message is split among the
lines of the sign without regard to spaces or punctuation. Only the last line of the sign may contain fewer
characters than the width indicated by the constructor parameter.

In addition to the constructor, the Sign class contains two methods.

The numberOfLines method returns an int representing the number of lines needed to display the
text on the sign. In the previous examples, numberOfLines would return 3, 2, and 1, respectively,
for the sign widths shown in the table.

The getLines method returns a String containing the message broken into lines separated by
semicolons (;) or returns null if the message is the empty string. The constructor parameter that
contains the message to be displayed will not include any semicolons. As an example, in the first row of the
preceding table, getLines would return "Everything on s;ale, please com;e in".
No semicolon should appear at the end of the String returned by getLines.

Hints: 
    Refer to detailed instructions and examples in the following PDF:
    https://apcentral.collegeboard.org/media/pdf/ap23-frq-comp-sci-a.pdf

    Python String methods:
    https://www.w3schools.com/python/python_ref_string.asp

    Python String Escape Characters:
    https://www.w3schools.com/python/gloss_python_escape_characters.asp

"""

class Sign():

    #code goes here