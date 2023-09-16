'''
Crie um programa que leia o preço de um produto, calcule e mostre o seu 
PREÇO PROMOCIONAL, com 5% de desconto.
'''

from funcoes import *

preco = coringa(float, 'DIgite o preço do produto: ')

desconto = preco - (( preco * 5) / 100) 

print(f'O produto com 5% de desconto fica R${desconto:.2f}')