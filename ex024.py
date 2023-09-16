'''
 Faça um algoritmo que pergunte a distância que um passageiro deseja 
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
viagens até 200Km e R$0.45 para viagens mais longas.
'''

from funcoes import *

distancia = coringa('Digite a distancia desejada em km: ', float)

if distancia <= 200:
    valor = distancia * 0.5
    
    print(f'Preço para pagar custando R$0.50 cada km: {valor:.2f}')
    
else:
    valor = distancia * 0.45
    
    print(f'Preço para pagar custando R$0.45 cada km: {valor:.2f}')