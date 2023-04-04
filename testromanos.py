import unittest

from conversor import RomantoDecimal


class TestRomanToDecimal(unittest.TestCase):
    def testRomanI(self):
        roman = RomantoDecimal('I')
        self.assertEqual(roman.roman_to_int(), 1)

    def testRomanII(self):
        roman = RomantoDecimal('II')
        self.assertEqual(roman.roman_to_int(), 2)

    def testRomanIV(self):
        roman = RomantoDecimal('IV')
        self.assertEqual(roman.roman_to_int(), 4)

    def testRomanIX(self):
        roman = RomantoDecimal('IX')
        self.assertEqual(roman.roman_to_int(), 9)

    def testRomanX(self):
        roman = RomantoDecimal('X')
        self.assertEqual(roman.roman_to_int(), 10)

    def testRomanL(self):
        roman = RomantoDecimal('L')
        self.assertEqual(roman.roman_to_int(), 50)

    def testRomanCMXCIX(self):
        roman = RomantoDecimal('CMXCIX')
        self.assertEqual(roman.roman_to_int(), 999)


if __name__ == '__main__':
    unittest.main()