from random import randint

class Matriz:

    def __init__(self, linhas, colunas, dados = None):
        self._linhas = linhas
        self._colunas = colunas
        
        if dados not is None
            self._dados = dados
        else
            self._dados = [[0 for x in range(linhas)] for y in range(colunas)]
        
    def criarMatrizComDadosAleatorios(self, linhas, colunas):
        matrix = [[0 for x in range(linhas)] for y in range(colunas)] 
        for i in range(0, linhas):
            for j in range(0, colunas):
                matrix[i][j] = randint(0,9)
        return matrix
    
    def identidade(dimensao)
        matrizIdentidade = Matriz(dimensao,dimensao)
        for i in range(dimensao)
            matrizIdentidade[i][i] = 1
        return matrizIdentidade