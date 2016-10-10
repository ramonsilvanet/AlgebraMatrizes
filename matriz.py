import copy
class Matriz:

    #Inicaliza o objeto matriz com os dados fornecidos ou retorna um matriz zerada
    def __init__(self, linhas, colunas, dados, resultados):

        if not (dados is None):
            self._linhas = len(dados)
            self._colunas = len(dados[0])
            self._dados = dados
            self._resultados = resultados

    #Calcula a matriz identidade
    def identidade(self, dimensao):
        matrizIdentidade = Matriz(dimensao,dimensao)
        for i in range(dimensao):
            matrizIdentidade[i][i] = 1
        return matrizIdentidade
    
    #calcula a determinante da matriz
    def determinante(self, dados):
        numeroDeLinhas = len(dados)
        if numeroDeLinhas > 2:
            i = 1
            t = 0
            soma = 0
            while t <= numeroDeLinhas - 1:
                d = {}
                t1 = 1
                while t1 <= numeroDeLinhas - 1:
                    m = 0
                    d[t1] = []
                    while m <= numeroDeLinhas - 1:
                        if (m != t):
                            d[t1].append(dados[t1][m])
                        m += 1
                    t1 += 1
                auxiliar = [d[x] for x in d]
                soma += i * (dados[0][t]) * (self.determinante(auxiliar))
                i *= -1
                t += 1
            return soma
        else:
            return dados[0][0] * dados[1][1] - dados[0][1] * dados[1][0]

    def substituirColuna(self, dados, coluna, posicao):
        aux = [[dados[x][y] for y in range(len(dados[0]))] for x in range(len(dados))]

        for x in range(len(dados)):
            aux[x][posicao] = coluna[x]
        return aux

