from funcoes import *

nome = input('Digite seu nome: ')
salario = coringa(float, 'Digite seu salário: ')

print(f'{nome} possui um salário de R${salario:.2f}')