'''

DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
Analise seus comprimentos e diga se é possível formar um triângulo com essas 
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento 
de cada lado deve ser menor que a soma dos outros dois.
'''

from funcoes import *

a = coringa('Lado a do triangulo', float)
b = coringa('Lado b do triangulo', float)
c = coringa('Lado c do triangulo', float)


if a < b + c and b < a + c and c < b + a:
    print('Triangulo')
    
else:
    print('Não sei qeu coisa é essa')