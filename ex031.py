'''
[DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
'''

from random import randint
from funcoes import *


while True:
    es = ['pedra', 'papel', 'tesoura']
    escolha = menuJoKenPo()
    
    ai = es[randint(0, len(es))]
    
    if ai == escolha:
        print('empate')
        
    elif escolha == 'pedra' and ai == 'tesoura':
        print('voce ganhou')
        
    elif escolha == 'pedra' and ai == 'papel':
        print('voce perdeu')
        
    elif escolha == 'papel' and ai == 'pedra':
        print('ganhou')
    
    elif escolha == 'papel' and ai == 'tesoura':
        print('perdeu')
        
    elif escolha == 'tesoura' and ai == 'pedra':
        print('perdeu')
    
    elif escolha == 'tesoura' and ai == 'papel':
        print('ganhou')