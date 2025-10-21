"""
¿POR QUÉ LA CONDICIÓN FINAL ES INCORRECTA?
"""

pares = []
for i in range(10):
    if i % 2 == 0:
        pares.append(i)
    else:
        continue
print(len(pares) == 10)
