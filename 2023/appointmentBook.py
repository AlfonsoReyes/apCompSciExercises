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
1. This question involves the AppointmentBook class, which provides methods for students to schedule
appointments with their teacher. Appointments can be scheduled during one of eight class periods during the
school day, numbered 1 through 8. A requested appointment has a duration, which is the number of minutes
the appointment will last. The 60 minutes within a period are numbered 0 through 59. In order for an
appointment to be scheduled, the teacher must have a block of consecutive, available minutes that contains at
least the requested number of minutes in a requested period. Scheduled appointments must start and end
within the same period.
"""

class AppointmentBook():

    def __init__(self, numPeriods=8, periodDuration=60, periodAppointments:list[list[(int,int)]]=None):
        """Constructor

        Args:
            self: obj instance
            numPeriods: int, must be > 0
            periodDuration: int, must be > 0
            periodAppointments: list[list[(int,int)]]
        """        
        
        self.numPeriods = numPeriods
        self.periodDuration = periodDuration

        #for this scenario, appointment instance will be a tuple consisting of two values:
        #   - minuteStart: int, can range from 0 to periodDuration
        #   - minuteEnd: int

        if periodAppointments is None:
            self.periodAppointments = [[] for x in range(numPeriods)]
        else:
            self.periodAppointments = periodAppointments

    def isMinuteFree(self, period:int, minute:int) -> bool:
        """DO NOT MAKE ANY ALTERATIONS TO THIS FUNCTION

        * Returns true if minute in period is available for an appointment and returns
        * false otherwise
        * Preconditions: 1 <= period <= 8; 0 <= minute <= 59
        """

        #input validation
        if period <= 0 or period > self.numPeriods or minute < 0 or minute >= self.periodDuration:
            raise Exception("Invalid period or minute args.")

        #get appointments list for given period
        appointments = self.periodAppointments[period-1]

        #check each appointment for given period to see if given minute is within any of the appointment blocks
        for appointment in appointments:

            start   = appointment[0]
            end     = appointment[1]

            #if given minute is within bounds (inclusive) of appointment tuple, then minute is not free
            if minute >= start and minute <= end:
                return False

        #if no cases found for given period and minute where there is overlap with existing appointment tuple,
        #   then the period/minute combo is free
        return True
    
    def reserveBlock(self, period:int, startMinute:int, duration:int):
        """DO NOT MAKE ANY ALTERATIONS TO THIS FUNCTION

        * Marks the block of minutes that starts at startMinute in period and
        * is duration minutes long as reserved for an appointment
        * Preconditions: 1 <= period <= 8; 0 <= startMinute <= 59;
        * 1 <= duration <= 60
        """

        #assuming that prevalidation was completed earlier
        #note that the start minute is included in duration, such that if startMinute is 50
        #   that minute  50 itself counts as part of the duration

        endMinute = startMinute + duration - 1
        self.periodAppointments[period-1].append((startMinute, endMinute))        
    
    def findFreeBlock(self, period:int, duration:int) -> int:
        """
        * Searches for the first block of duration free minutes during period, as described in
        * part (a). Returns the first minute in the block if such a block is found or returns -1 if no
        * such block is found.
        * Preconditions: 1 <= period <= 8; 1 <= duration <= 60
        """

        #your code goes here

        return
    
    def makeAppointment(self, startPeriod:int, endPeriod:int, duration:int) -> int:
        """
        * Searches periods from startPeriod to endPeriod, inclusive, for a block
        * of duration free minutes, as described in part (b). If such a block is found,
        * calls reserveBlock to reserve the block of minutes and returns true; otherwise
        * returns false.
        * Preconditions: 1 <= startPeriod <= endPeriod <= 8; 1 <= duration <= 60
        """
       
        #your code goes here

        return
    