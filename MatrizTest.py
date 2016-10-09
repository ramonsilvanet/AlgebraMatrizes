import unittest
from matriz import Matriz

class MatrizTest(unittest.TestCase):

    def testCalcularDeterminante(self):
        dados = [[1, 2, 1], [2, -1, 1], [3, 1, -1]]
        self.matriz = Matriz(3, 3, dados)
        self.assertEqual(15, self.matriz.calcularDeterminante())

    if __name__ == '__main__':
        unittest.main()