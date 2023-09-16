'''
 A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
'''

from funcoes import *

kmpercorrido = coringa(float, "Digite os km percorridos: ")

dias = coringa(int, 'Dias usando o carro: ')

preco = (90 * dias) + (kmpercorrido * 0.2)

print(f'Preço total pelo aluguél do carro: R${preco:.2f}')