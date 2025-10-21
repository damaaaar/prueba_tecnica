"""
ARREGLA EL ERROR Y HACE QUE FUNCIONA PARA CUALQUIER NUMERO ENTERO POSITIVO
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
