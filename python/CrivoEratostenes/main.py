import math

num = int(input("Primos até o número: "))

# Cria um vetor de valores True
primos = []
for i in range(num + 1):
    primos.append(True)

primos[0] = False
primos[1] = False
# Define o valor máximo que será avaliado
maximo = int(math.sqrt(num))

# Algoritmo do crivo
for i in range(maximo + 1):
    if primos[i]:
        for j in range(i * 2, num + 1, i):
            primos[j] = False

# Apresenta os resultados
total = 0
for i in range(2, num + 1):
    if primos[i]:
        total += 1
        print(i, end=' ')
print()
print(total)