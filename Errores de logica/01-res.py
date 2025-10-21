"""
LA VARIABLE 'suma' DEBE ALMACENAR LA SUMA DE TODOS LOS ELEMENTOS DEL
ARREGLO 'numeros'.
"""

numeros = [1, 2, 3, 4, 5]
suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
print(suma)

"""
RESPUESTA:
SE ESTÁ SUMANDO LA VARIABLE DE CONTROL, NO EL CONTENIDO DEL ARREGLO
"""
