import unittest
from datetime import datetime
from lib.parser import isPuzzleReleased

class Tests_isPuzzleReleased(unittest.TestCase):
    def test_DayInPast_2022(self):
        today = datetime(2022, 12, 17)
        day = 2
        self.assertEqual(isPuzzleReleased(today, day), True)
        
    def test_DayInFuture_2022(self):
        today = datetime(2022, 12, 17)
        day = 21

        self.assertEqual(isPuzzleReleased(today, day), False)
        
    def test_PresentDay_2022(self):
        today = datetime(2022, 12, 17)
        day = 17
        self.assertEqual(isPuzzleReleased(today, day), True)
        
    def test_DayInPast_After2022(self):
        today = datetime(2023, 12, 17)
        day = 17
        self.assertEqual(isPuzzleReleased(today, day), True)


if __name__ == '__main__':
    unittest.main()