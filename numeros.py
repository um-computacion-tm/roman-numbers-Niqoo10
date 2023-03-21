import unittest
import math

def decimal_to_roman(decimal):

Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
N=int(input("Ingresa numero entero\n"))
u= N % 10
d=int(math.floor(N/10))%10
c=int(math.floor(N/100))
if(N>=100): 
 print(Centena[c]+Decena[d]+Unidad[u])
else:
 if(N>=10):
  print(Decena[d]+Unidad[u])
 else:
  print(Unidad[N])


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


if __name__ == '__main__':
    unittest.main()

