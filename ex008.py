from funcoes import *


metros = coringa(float, 'Digite um valor em metros: ')

dm = metros * 10
cm = metros * 100
mm = metros * 1000

dam = metros / 10
hm = metros / 100
km = metros / 1000

print(f'{metros}m corresponde a: ')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')
print(f'{dam}dam')
print(f'{hm}hm')
print(f'{km}km')
