import unittest
from lib.parser import argParser

class Tests_argParser_ShortFlags_Correct(unittest.TestCase):
    def test_day(self):
        args = ['-d', '1', '-p', '2']
        day, _, __ = argParser(args)
        self.assertEqual(day, 1)

    def test_part(self):
        args = ['-d', '1', '-p', '2']
        _, part, __ = argParser(args)

        self.assertEqual(part, 2)
        
    def test_testData(self):
        args = ['-d', '1', '-p', '2', '-t']
        _, __, test = argParser(args)

        self.assertEqual(test, True)

    def test_challengeData(self):
        args = ['-d', '1', '-p', '2']
        _, __, noTest = argParser(args)

        self.assertEqual(noTest, False)

class Tests_argParser_LongFlags_Correct(unittest.TestCase):
    def test_day(self):
        args = ['--day', '1', '--part', '2']
        day, _, __ = argParser(args)
        self.assertEqual(day, 1)

    def test_part(self):
        args = ['--day', '1', '--part', '2']
        _, part, __ = argParser(args)

        self.assertEqual(part, 2)
        
    def test_testData(self):
        args = ['--day', '1', '--part', '2', '--test']
        _, __, test = argParser(args)

        self.assertEqual(test, True)

    def test_challengeData(self):
        args = ['--day', '1', '--part', '2']
        _, __, noTest = argParser(args)

        self.assertEqual(noTest, False)

class Tests_argParser_DuplicateFlag_Correct(unittest.TestCase):
    def test_dayFlag(self):
        args = ['--day', '1', '--part', '2', '-d', '2']
        day, _, __ = argParser(args)
        self.assertEqual(day, 2)

    def test_partFlag(self):
        args = ['--day', '1', '-p', '1', '--part', '2']
        _, part, __ = argParser(args)

        self.assertEqual(part, 2)
        
    def test_testFlag(self):
        args = ['--day', '1', '--part', '2', '--test', '-t']
        _, __, test = argParser(args)

        self.assertEqual(test, True)

class Tests_argParser_InvalidPart_Error(unittest.TestCase):
    def test_PartZero(self):
        args = ['--day', '1', '--part', '0']
        self.assertRaisesRegex(Exception, "Puzzle part must be 1 or 2.", argParser, args)

    def test_PartLargerThanTwo(self):
        args = ['--day', '1', '--part', '3']
        self.assertRaisesRegex(Exception, "Puzzle part must be 1 or 2.", argParser, args)
        
class Tests_argParser_InvalidDay_Error(unittest.TestCase):
    def test_DayZero(self):
        args = ['--day', '0', '--part', '1']
        self.assertRaisesRegex(Exception, "Invalid day selected.", argParser, args)
        
    def test_DayAfterChristmas(self):
        args = ['--day', '26', '--part', '1']
        self.assertRaisesRegex(Exception, "Invalid day selected.", argParser, args)
        
    def test_InvalidDayAndPart(self):
        args = ['--day', '26', '--part', '3']
        self.assertRaisesRegex(Exception, "Invalid day selected.", argParser, args)

class Tests_argParser_MissingArgument_Error(unittest.TestCase):
    def test_MissingDay(self):
        args = ['--part', '1']
        self.assertRaisesRegex(Exception, "Missing argument for -d/--day", argParser, args)
        
    def test_MissingPart(self):
        args = ['--day', '1']
        self.assertRaisesRegex(Exception, "Missing argument for -p/--part", argParser, args)

    def test_MissingArgument_DuplicateFlags(self):
        args = ['--day', '1', '-p', '2', '-d', '-p']
        self.assertRaisesRegex(Exception, "Missing argument for -d/--day/-p/--part", argParser, args)
        
    def test_MissingDay_InvalidDay(self):
        args = ['--day', '1', '-p', '2', '-d', '31', '-d']
        self.assertRaisesRegex(Exception, "Missing argument for -d/--day", argParser, args)

    def test_MissingPart_InvalidPart(self):
        args = ['--day', '1', '-p', '2', '-p', '31', '-p']
        self.assertRaisesRegex(Exception, "Missing argument for -p/--part", argParser, args)

class Tests_argParser_UnrecognizedArguments_Error(unittest.TestCase):
    def test_NegativePart(self):
        args = ['--day', '1', '--part', '-1']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: -1", argParser, args)
        
    def test_UnrecognizedArgument(self):
        args = ['--day', '1', '--part', '1', '--notanargument']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: --notanargument", argParser, args)
        
    def test_UnrecognizedArgument_MissingPart(self):
        args = ['--day', '1', '--part', '--notanargument']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: --notanargument", argParser, args)

    def test_UnrecognizedArgument_MissingDay(self):
        args = ['--day', '--part', '1', '--notanargument']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: --notanargument", argParser, args)
        
    def test_UnrecognizedArgument_InvalidDay(self):
        args = ['--day', '31', '--part', '1', '--notanargument']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: --notanargument", argParser, args)
        
    def test_UnrecognizedArgument_InvalidPart(self):
        args = ['--day', '1', '--part', '31', '--notanargument']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: --notanargument", argParser, args)
        
    def test_DayNotANumber(self):
        args = ['--day', '1', '--part', 'a']
        self.assertRaisesRegex(Exception, "Unrecognized arguments: a", argParser, args)
    
if __name__ == '__main__':
    unittest.main()