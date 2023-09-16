'''
 Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
dela e depois mostre se ela pode ou não votar.
'''
from funcoes import *

ano = coringa(int, 'Digite o ano de nascimento: ')

idade = 2023 - ano


if idade  < 18:
    print('Proibido votar')
    
else:
    print('Voto liberado')

