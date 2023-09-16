def x():
    from os import system
    
    system('cls')


def coringa (txt = '', tipo = ''):
    while True:
        
        try:
            if tipo == '':
                a = input(txt)
            else:
                a = tipo(input(txt))
            
        except:
            x()
            print('Digite um valor válido')
            
        else:
            return a
        
        
def menuSexo ():
    print('Escolha seu sexo\n')
    sexo = ['Homem', 'Mulher']
    
    while True:
        for sex in range(0, len(sexo)):
            print(f'{sex + 1} -------- {sexo[sex]}')
            
        escolha = coringa('Sua opção: ', int) - 1
        
        if escolha < len(sexo):
            x()
            print('Digite uma opção válida')
            
        else:
            return sexo[escolha]
        
        
def menuJoKenPo ():
    print('Escolha seu sexo\n')
    es = ['pedra', 'papel', 'tesoura']
    
    while True:
        for s in range(0, len(es)):
            print(f'{s + 1} -------- {es[s]}')
            
        escolha = coringa('Sua opção: ', int) - 1
        
        if escolha < len(es):
            x()
            print('Digite uma opção válida')
            
        else:
            return es[escolha]