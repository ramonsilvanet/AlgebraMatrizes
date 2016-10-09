from matriz import Matriz

dados = [[1,2,1], [2,-1,1], [3,1,-1]]
m = Matriz(3, 3, dados)

print m.calcularDeterminante()