"""
LA VARIABLE 'suma' DEBE ALMACENAR LA SUMA DE TODOS LOS ELEMENTOS DEL
ARREGLO 'numeros'.
"""

numeros = [1, 2, 3, 4, 5]
suma = 0
for i in range(len(numeros)):
    suma += i

print(suma)
