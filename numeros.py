import unittest

#PARTE DE CODIGO
def decimal_to_roman(num):
 
    c = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    x = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    i = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]

    centena = c[(num % 1000) // 100]
    decena = x[(num % 100) // 10]
    unidad = i[num % 10]

    resultado = ( centena + decena + unidad)
    return resultado


#PARTE DE TEST
class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_quince(self):
        resultado = decimal_to_roman(15)
        self.assertEqual(resultado, 'XV')

    def test_veinte(self):
        resultado = decimal_to_roman(20)
        self.assertEqual(resultado, 'XX')

    def test_treintaycuatro(self):
        resultado = decimal_to_roman(34)
        self.assertEqual(resultado, 'XXXIV')

    def test_cincuenta(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')

    def test_noventaynueve(self):
        resultado = decimal_to_roman(99)
        self.assertEqual(resultado, 'XCIX')

    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_novecientonoventaynueve(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado, 'CMXCIX')


if __name__ == '__main__':
    unittest.main()

