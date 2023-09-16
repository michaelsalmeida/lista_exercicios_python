'''
 Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
jogador vai tentar descobrir qual foi o valor sorteado.
'''

from random import randint
from funcoes import *

ai = randint(1, 5)
escolha = coringa('Advinhe o numero que eu pensei: ', int)

if escolha == ai:
    print('Acertou')
    
else:
    print(f'Errou, pensei no {ai}')