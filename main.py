from matriz import Matriz

dados = [[1,2,1], [2,-1,1], [3,1,-1]]
resultados = [8,3,2]
m = Matriz(3, 3, dados, resultados)

m.regraDeCrammer()