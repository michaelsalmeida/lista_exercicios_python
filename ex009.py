'''
Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
'''

from funcoes import *

dinheiro = coringa(float, 'Digite o dinheiro que voce tem na carteira: ')

dolar = dinheiro / 3.45

print(f'Com R${dinheiro:.2f} voce pode comprar US${dolar:.2f}')