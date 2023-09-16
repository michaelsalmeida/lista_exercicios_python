'''
 Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em 
um vetor. No final, mostre: 
a) Qual é a média da turma
b) Quantos alunos estão acima da média da turma
c) Qual foi a maior nota digitada
d) Em que posições a maior nota aparece
'''

from funcoes import *

notas = []
posicoesmaiornota = []
soma = 0

maior = 0

qtdacimadamedia = 0

for nota in range(0, 10):
    n = coringa('Digite a nota: ', float)
    soma += n
    notas.append(n)
    
    if nota == 0:
        maior = n
    
    elif n > maior:
        maior = n
        
media = soma / 10
    
for no in range(0, len(notas)):
    if notas[no] >  media:
        qtdacimadamedia += 1
        
    if no == maior:
        posicoesmaiornota.append(no)
        

print(f'Média da turma: {media}')
print(f'Alunos acima da média: {qtdacimadamedia}')
print(f'Maior nota digitada: {maior}')
print(f'Posicoes aonde a maior nota está: {posicoesmaiornota}')