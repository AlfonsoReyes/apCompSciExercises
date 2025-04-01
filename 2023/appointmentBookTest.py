from appointmentBook import AppointmentBook
import random
import math
import unittest

class AppointmentBookTest(unittest.TestCase):

    def testFindFreeBlockOne(self):
        """
        0–9 (10 minutes) No
        10–14 (5 minutes) Yes
        15–29 (15 minutes) No
        30–44 (15 minutes) Yes
        45–49 (5 minutes) No
        50–59 (10 minutes) Yes
        """

        blocks = [
            [],
            [(0,9), (15,29), (45,49)],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        ab = AppointmentBook(8, 60, [])

        startMinute = ab.findFreeBlock(2, 15)

        self.assertEqual(startMinute, 30, "Invalid result for findFreeBlock function! Expected output of 30 for findFreeBlock(2, 15)")

    def testFindFreeBlockTwo(self):
        """
        0–9 (10 minutes) No
        10–14 (5 minutes) Yes
        15–29 (15 minutes) No
        30–44 (15 minutes) Yes
        45–49 (5 minutes) No
        50–59 (10 minutes) Yes
        """

        blocks = [
            [],
            [(0,9), (15,29), (45,49)],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        ab = AppointmentBook(8, 60, [])

        startMinute = ab.findFreeBlock(2, 9)

        self.assertEqual(startMinute, 30, "Invalid result for findFreeBlock function! Expected output of 30 for findFreeBlock(2, 9)")

    def testFindFreeBlockThree(self):
        """
        0–9 (10 minutes) No
        10–14 (5 minutes) Yes
        15–29 (15 minutes) No
        30–44 (15 minutes) Yes
        45–49 (5 minutes) No
        50–59 (10 minutes) Yes
        """

        blocks = [
            [],
            [(0,9), (15,29), (45,49)],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        ab = AppointmentBook(8, 60, blocks)

        startMinute = ab.findFreeBlock(2, 20)

        self.assertEqual(startMinute, 30, "Invalid result for findFreeBlock function! Expected output of -1 for findFreeBlock(2, 20)")

    def testMakeAppointmentOne(self):
        """
        Period Minutes Available?
        2 0–24 (25 minutes) No
        2 25–29 (5 minutes) Yes
        2 30–59 (30 minutes) No
        3 0–14 (15 minutes) Yes
        3 15–40 (26 minutes) No
        3 41–59 (19 minutes) Yes
        4 0–4 (5 minutes) No
        4 5–29 (25 minutes) Yes
        4 30–43 (14 minutes) No
        4 44–59 (16 minutes) Yes
        """

        blocks = [
            [],
            [(0, 24), (30, 59)],
            [(15, 40)],
            [(0, 4), (30, 43)],
            [],
            [],
            [],
            []
        ]
        ab = AppointmentBook(8, 60, blocks)

        #The method call makeAppointment(2, 4, 22) returns true and results in the minutes 5
        #through 26, inclusive, in period 4 being marked as unavailable
        appointmentMade = ab.makeAppointment(2, 4, 22)

        self.assertEqual(appointmentMade, True, "Invalid result for makeAppointment(2, 4, 22). Expected true.")

    def testMakeAppointmentTwo(self):
        """
        Period Minutes Available?
        2 0–24 (25 minutes) No
        2 25–29 (5 minutes) Yes
        2 30–59 (30 minutes) No
        3 0–14 (15 minutes) Yes
        3 15–40 (26 minutes) No
        3 41–59 (19 minutes) Yes
        4 0–4 (5 minutes) No
        4 5–29 (25 minutes) Yes
        4 30–43 (14 minutes) No
        4 44–59 (16 minutes) Yes
        """

        blocks = [
            [],
            [(0, 24), (30, 59)],
            [(15, 40)],
            [(0, 4), (30, 43)],
            [],
            [],
            [],
            []
        ]
        ab = AppointmentBook(8, 60, blocks)

        # The method call makeAppointment(3, 4, 3) returns true and results in the 
        # minutes 0 through 2, inclusive, in period 3 being marked as unavailable.        
        appointmentMade = ab.makeAppointment(3, 4, 3)

        self.assertEqual(appointmentMade, True, "Invalid result for makeAppointment(3, 4, 3). Expected true.")

    def testMakeAppointmentThree(self):
        """
        Period Minutes Available?
        2 0–24 (25 minutes) No
        2 25–29 (5 minutes) Yes
        2 30–59 (30 minutes) No
        3 0–14 (15 minutes) Yes
        3 15–40 (26 minutes) No
        3 41–59 (19 minutes) Yes
        4 0–4 (5 minutes) No
        4 5–29 (25 minutes) Yes
        4 30–43 (14 minutes) No
        4 44–59 (16 minutes) Yes
        """

        blocks = [
            [],
            [(0, 24), (30, 59)],
            [(15, 40)],
            [(0, 4), (30, 43)],
            [],
            [],
            [],
            []
        ]
        ab = AppointmentBook(8, 60, blocks)

        # The method call makeAppointment(2, 4, 30) returns false, since there is no block of 30
        # available minutes in periods 2, 3, or 4
        appointmentMade = ab.makeAppointment(2, 4, 30)

        self.assertEqual(appointmentMade, False, "Invalid result for makeAppointment(2, 4, 30). Expected false.")

def buildAppointmentBook():
    """Validate creation of AppointmentBook class and its default implemented functions.
    """

    periods = 8
    ab = AppointmentBook(periods, 60)
    duration = 5

    for period in range(1, periods+1, 1):
        print(period)
        
        for i in range(5):

            startMinute = round(random.random() * 54)
            minutes = range(startMinute, startMinute + duration, 1)

            createNewAppointment = True
            for minute in minutes:
                if not ab._isMinuteFree(period, minute):
                    createNewAppointment = False
            
            if createNewAppointment:
                ab._reserveBlock(period, startMinute, duration)

        # for appointment in ab.periodAppointments[period-1]:
        #     print(f"\t{appointment}")


    for period in range(1, periods+1, 1):
        ab.periodAppointments[period-1].sort(key=lambda app: app[0])
        print(f"Period: {period}")

        for appointment in ab.periodAppointments[period-1]:
           print(f"\t{appointment}")


if __name__ == '__main__':
    #unittest.main()
    buildAppointmentBook()

