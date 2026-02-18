palavra = input('Entre a palavra: ')
palavra = palavra.strip().lower()
for i in range(50):
    print()
erros = ''
acertos = ''
fim = False
while not fim:
    resposta = ''
    for aux in palavra:
        if aux in acertos:
            resposta += aux
            print(aux, end=' ')
        else:
            print('_', end=' ')
    print()
    for aux in erros:
        print(aux, end=' ')
    print()
    if resposta == palavra:
        print('Parabéns, você venceu!')
        fim = True
    elif len(erros) >= 6:
        print('Perdeu! A palavra era', palavra)
        fim = True
    else:
        letra = input('entre uma letra: ')
        letra = letra.strip().lower()[0]
        if letra in acertos or letra in erros:
            print('Você já tentou essa letra!')
        if letra in palavra:
            acertos += letra
        elif letra not in erros:
            erros += letra
