'''
Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
BISSEXTO.
'''

from funcoes import *

ano = coringa('Digite um ano: ', int)

if ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto')
    
else:
    print('Não bissexto') 