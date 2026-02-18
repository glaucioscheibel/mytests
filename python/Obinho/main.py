entrada = input('Informe a sequencia de lajotas:')
C = []
for lajota in entrada:
    C.append(lajota == '1')
if not C[0] or not C[len(C) - 1]:
    print('Deve iniciar e finalizar com 1!')
elif len(C) > 10**4:
    print('O tamanho máximo da entrada é 10000')
else:
    pulos = 0
    posicao = 0
    while posicao < len(C) - 1:
        if posicao < len(C) - 2 and C[posicao + 2]:
            posicao += 2
        elif C[posicao + 1]:
            posicao += 1
        else:
            pulos = -1
            break
        pulos += 1
print(pulos)