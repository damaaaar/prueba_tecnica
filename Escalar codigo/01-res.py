"""
MODIFICA EL CÓDIGO PARA QUE ACEPTE n CANTIDAD DE PARÁMETROS.
"""


def promedio(*args):
    return sum(args) / len(args)


res = promedio(12, 3, 9, 3, 1, 9, 10, 21)
print(res)
