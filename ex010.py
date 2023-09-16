'''
Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
'''

from funcoes import *

altura = coringa(float, 'Digite a altura da parede: ')
largura = coringa(float, 'Digite a largura da parede: ')

area = altura * largura

litros = area / 2

print(f'Usa {litros:.2f}L de tinta para pintar uma parede de área {area}m')