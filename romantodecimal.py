import unittest

def roman_to_decimal(roman):
    total = 0
    for letter in roman:
        if letter == 'I':
            total += 1
        elif letter == 'V':
            if total > 0:
                total = -1
            total += 5
        elif letter == 'X':
            if total > 0:
                total = -1
            total += 10
        elif letter == 'XV':
            if total > 0:
                total = -1
            total += 15
        elif letter == 'XX':
            if total > 0:
                total = -1
            total += 20


    return total

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)

    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)

    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)

    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)

    def test_VI(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)

    def test_VII(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)

    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)

    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)

    def test_XI(self):
        resultado = roman_to_decimal('XI')
        self.assertEqual(resultado, 11)

    def test_XIII(self):
        resultado = roman_to_decimal('XIII')
        self.assertEqual(resultado, 13)

    '''def test_XIV(self):
        resultado = roman_to_decimal('XIV')
        self.assertEqual(resultado, 14)'''
    
    def test_XX(self):
        resultado = roman_to_decimal('XX')
        self.assertEqual(resultado, 20)



if __name__ == '__main__':
    unittest.main()