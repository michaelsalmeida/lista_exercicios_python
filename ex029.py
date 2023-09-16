'''
 Desenvolva um programa que leia o nome de um funcionário, seu salário, 
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%
'''

from funcoes import *

nome = coringa('Seu nome: ')
anosEmpresa = coringa('Anos na empresa: ', int)
salario = coringa('Salario: ', float)

if anosEmpresa <= 3:
    reajuste = salario + ((salario * 3) / 100)
    print(f'Salário reajustado: {reajuste:.2f}')
    
elif 3 < anosEmpresa < 10:
    reajuste = salario + ((salario * 12.5) / 100)
    print(f'Salário reajustado: {reajuste:.2f}')
    
else:
    reajuste = salario + ((salario * 20) / 100)
    print(f'Salário reajustado: {reajuste:.2f}')