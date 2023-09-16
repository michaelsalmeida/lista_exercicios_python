'''
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um 
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
quantos dias de vida um fumante perderá e exiba o total em dias.
'''

from funcoes import *

qtdcigarro = coringa(int, 'Quantos cigarros você fumou por dia: ')
anos = coringa(int, 'Quantos anos voce fumou: ')

totalcigarro = qtdcigarro * (anos * 365)

diasperdidos = (((totalcigarro * 10) / 60) / 24)

print(f'Voce fumou {qtdcigarro} durante {anos} anos por isso voce perdeu {diasperdidos:.2f} dias de vida')
