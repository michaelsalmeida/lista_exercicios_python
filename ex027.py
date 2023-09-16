'''
Crie um programa que leia duas notas de um aluno e calcule a sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO
'''

from funcoes import *

n1 = coringa('Primeira nota: ', int)
n2 = coringa('Segunda nota: ', int)

media = (n1 + n2) / 2

if media <= 4.9:
    print('Reprovado')
    
elif 5.0 >= media <= 6.9:
    print('Recuperação')
    
else:
    print('Aprovado')