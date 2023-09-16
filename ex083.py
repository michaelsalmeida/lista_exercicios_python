'''
 [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números 
aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os 
números gerados e depois coloque o vetor em ordem crescente, mostrando no final 
os valores ordenados.
'''

from funcoes import *
from random import randint

aleatorios = []

for numero in range(0, 20):
    aleatorios.append(randint(0, 99))
    
    
print(f'Lista sem organizar: {aleatorios}')

aleatorios.sort()

print(f'Lista organizada: {aleatorios}')