"""
QUE VA A PASAR SI DOS NÚMEROS SON IGUALES
"""


def maximo(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


res = maximo(5, 5, 3)
print(res)
