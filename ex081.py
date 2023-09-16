'''
Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No 
final, mostre:
a) Qual é a média de idade das pessoas cadastradas
b) Em quais posições temos pessoas com mais de 25 anos
c) Qual foi a maior idade digitada (podem haver repetições)
d) Em que posições digitamos a maior idade
'''

from funcoes import *

idades = []
posicoes25 = []
posicoesmaioridade = []

for id in range(0, 8):
    idad = coringa('Digite a idade: ', int)
    idades.append(idad)
    
soma = 0

maior = 0
menor = 0

for numero in range(0, len(idades)):
    soma += idades[numero]
    
    
    if idades[numero] > 25:
        posicoes25.append(numero)
    
    
    if numero == 0:
        maior = idades[numero]
        menor = idades[numero]
        
media = soma / len(idades)
        
for num in range(0, len(idades)):
    if idades[num] == maior:
        posicoesmaioridade.append(num)  
        
        
        
print(f'Media as idades {media}')
print(f'Maior idade digitada: {maior}')
print(f'Posicoes de maior idade digitada: {posicoesmaioridade}')
print(f'Posicoes maiores que 25: {posicoes25}')
