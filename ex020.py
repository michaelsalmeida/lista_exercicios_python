'''
 Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
ÍMPAR.

'''

from funcoes import *

numero = coringa('Digite um número')

if numero % 2 == 0:
    print('Par')
    
else:
    print('impar')