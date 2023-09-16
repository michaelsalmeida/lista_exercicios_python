'''
Desenvolva uma lógica que leia os valores de A, B e C de uma equação do 
segundo grau e mostre o valor de Delta.
'''

from funcoes import *

a = coringa(int, 'Valor de A: ')
b = coringa(int, 'Valor de B: ')
c = coringa(int, 'Valor de C: ')

delta = (b ** 2) - 4 * a * c

print(f'O delta dessa equação é {delta}')