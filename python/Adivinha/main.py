"""
Faça um programa que peça ao usuário pensar em um número de 1 a 100.
O programa irá então tentar adivinhar o número pensado. A cada tentativa, o usuário irá responder se o programa acertou (C), o número é maior (M) ou se é menor (N).
"""

print('Pense em um número de 1 a 1000:')
input()

acertou = False
menor = 1
maior = 1000
tentativas = 0

while not acertou:
    tentativas = tentativas + 1
    chute = int((menor + maior) / 2)
    print(f'Você pensou o numero {chute}')
    resposta = input()
    if resposta == 'M': # direita
        menor = chute + 1
    elif resposta == 'N': # esquerda
        maior = chute - 1
    elif resposta == 'C':
        acertou = True

print(f'Sucesso, computador derrota humano em {tentativas} tentativas!')
