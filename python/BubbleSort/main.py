V = [6, 5, 3, 1, 8, 7, 2, 4]

trocou = True

tam = len(V) - 1

while trocou:
    trocou = False
    for i in range(0, tam):
        if V[i] > V[i + 1]:
            aux = V[i]
            V[i] = V[i + 1]
            V[i + 1] = aux
            trocou = True
    tam -= 1

print(V)
