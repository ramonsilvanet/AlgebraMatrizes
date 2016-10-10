import unittest
from matriz import Matriz
from crammer import Crammer

class MatrizTest(unittest.TestCase):

    def testCalcularDeterminante(self):
        dados = [[1, 2, 1], [2, -1, 1], [3, 1, -1]]
        conjuntosolucao = [8,3,2]
        determinanteDaMatriz = 15

        self.matriz = Matriz(3, 3, dados, conjuntosolucao)
        self.assertEquals(determinanteDaMatriz, self.matriz.determinante(self.matriz._dados))

    def testResoverUsandoCrammer(self):
        dados = [[1, 2, 1], [2, -1, 1], [3, 1, -1]]
        conjuntosolucao = [8, 3, 2]

        self.matriz = Matriz(3, 3, dados, conjuntosolucao)
        self.regra = Crammer()

        self.assertEquals([1,2,3], self.regra.resolver(self.matriz))

    if __name__ == '__main__':
        unittest.main()