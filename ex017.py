'''
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
'''

from funcoes import *

velocidade = coringa(float, 'Velocidade do carro: ')

if velocidade <= 80:
    print('Velocidade permitida')
    
else:
    multa = (velocidade - 80) * 5
    
    print(f'Multa de R${multa:.2f}')