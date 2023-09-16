'''
Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais
'''

from funcoes import *

n1 = coringa('Primeiro número: ', int)
n2 = coringa('Segundo número: ', int)


if n1 < n2 :
    print('Segunto número é maior')

elif n2 < n1:
    print('Primeiro número é maior')
    
else:
    print('Os 2 são iguais')