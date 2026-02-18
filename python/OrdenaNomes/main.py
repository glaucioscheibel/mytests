"""
Usando do algoritmo da bolha, ordene a lista de nomes do vetor nomes.
https://repl.it/@gscheibel/OrdenaNomes
"""
V = []

arquivo = open('nomes.txt')
for linha in arquivo:
    V.append(linha.strip())
arquivo.close()

troca = True
cont = 0
while troca:
    troca = False
    for i in range(len(V) - 1):
        cont += 1
        if V[i] > V[i + 1]:
            aux = V[i]
            V[i] = V[i + 1]
            V[i + 1] = aux
            troca = True
#print(V)
print(cont)
