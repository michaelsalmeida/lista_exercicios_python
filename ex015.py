'''
Crie um programa que leia o número de dias trabalhados em um mês e mostre o 
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 
por hora trabalhada.
'''

from funcoes import *

dias = coringa(int, 'Dias trabalhados: ')

salario = ( dias * 8 ) * 25

print(f'Salário recebido dirante {dias} dias de trabalho: R${salario:.2f}')