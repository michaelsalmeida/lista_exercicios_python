'''
 Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo 
que:
 - Homens ganham 5% de desconto
 - Mulheres ganham 13% de desconto
'''

from funcoes import *

nome = coringa('Digite seu nome')
sexo = menuSexo()
compras = coringa('Digite o valor da sua compra', float)


if sexo == 'Homem':
    desconto = compras - ((compras * 5) / 100)
    print(f'Por ser {sexo} suas compras ganharam 5% de desconto e ficaram R${desconto:.2f} ')
    
else:
    desconto = compras - ((compras * 13) / 100)
    print(f'Por ser {sexo} suas compras ganharam 13% de desconto e ficaram R${desconto:.2f} ')