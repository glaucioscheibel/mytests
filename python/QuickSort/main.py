from random import choice
cont = 0
def qsort(v):
    global cont
    if len(v) <= 1:
        return v
    menor = []
    igual = []
    maior = []
    pivo = choice(v)
    for i in v:
        cont += 1
        if i < pivo:
            menor.append(i)
        elif i > pivo:
            maior.append(i)
        else:
            igual.append(i)
    return qsort(menor) + igual + qsort(maior)

arq = open('nomes.txt')
lista = []
for linha in arq:
    lista.append(linha.strip().upper())
arq.close()

# print(lista)

lista = qsort(lista)
print(lista)
print("terminou")
print(cont)