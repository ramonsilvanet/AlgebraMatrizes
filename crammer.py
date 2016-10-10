class Crammer:

    def resolver(self, matriz):
        det = matriz.determinante(matriz._dados)

        matrizX = matriz.substituirColuna(matriz._dados, matriz._resultados, 0)
        detx = matriz.determinante(matrizX)

        matrizY = matriz.substituirColuna(matriz._dados, matriz._resultados, 1)
        dety = matriz.determinante(matrizY)

        matrizZ = matriz.substituirColuna(matriz._dados, matriz._resultados, 2)
        detz = matriz.determinante(matrizZ)

        return [detx / det, dety / det, detz / det]
