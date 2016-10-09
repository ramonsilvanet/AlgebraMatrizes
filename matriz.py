from random import randint

class Matriz:

    #Inicaliza o objeto matriz com os dados fornecidos ou retorna um matriz zerada
    def __init__(self, linhas, colunas, dados = None):
        self._linhas = linhas
        self._colunas = colunas
        
        if not (dados is None):
            self._dados = dados
        else:
            self._dados = [[0 for x in range(linhas)] for y in range(colunas)]
            
    #Calcula a matriz identidade
    def identidade(self, dimensao):
        matrizIdentidade = Matriz(dimensao,dimensao)
        for i in range(dimensao):
            matrizIdentidade[i][i] = 1
        return matrizIdentidade
    
    #calcula a determinante da matriz
    def calcularDeterminante(self):
        if self._linhas == 3 and self._colunas == 3:
            matriz = Matriz(self._linhas+2, self._colunas, self.expandirMatriz())
        else:
            matriz = Matriz(self._linhas, self._colunas, self._dados)

        determinante = 0
        for x in range(self._colunas):
            produto = 1
            for i in range(self._colunas):
                produto = produto * matriz._dados[i][i+x]
            determinante = determinante + produto
        return determinante

    def expandirMatriz(self):
        novaMatriz = [[0 for x in range(self._linhas + 2)] for y in range(self._colunas)]

        for i in range(0, self._linhas):
            for j in range(0, self._colunas):
                novaMatriz[i][j] = self._dados[i][j]
                if j <= (self._colunas - 2):
                    novaMatriz[i][self._colunas + j] = self._dados[i][j]
        return novaMatriz