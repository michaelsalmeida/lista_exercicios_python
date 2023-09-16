'''
 [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
de triângulo será formado: 
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
'''

from funcoes import *

a = coringa('Lado a do triangulo', float)
b = coringa('Lado b do triangulo', float)
c = coringa('Lado c do triangulo', float)


if a == b and a == c and b == c:
    print('equilatero')
    
elif a == b and a == c and b != c or b == a and b == c and a != c or c == a and c == b and b != c:
    print('isósceles')
    
else:
    print('Escaleno') 