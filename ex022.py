'''
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
alistamento.
'''

from funcoes import *

ano = coringa('Digite o ano de nascimento', int)

idade = 2023 - ano

if idade < 18:
    print(f'Falta {18 - idade} anos para voce poder se alistar')
    
elif idade == 18:
    print('Hoar de se alistar')
    
else:
    print(f'Já se passaram {idade - 18} anos pra voce se alistar')
    