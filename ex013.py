'''
Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
seu novo salário, com 15% de aumento.
'''

from funcoes import *

salario = coringa(float, "Digite seu salário: ")

aumento = salario + ((salario * 15) / 100)

print(f'O salário com o aumento ficará R${aumento}')