"""
Todos os dias um vetor com um milhão de números inteiros de 1 dígito é gerado. Neste vetor esconde-se a senha de 4 dígitos de abertura do cofre do Banco Tostão S/A. Um hacker conseguiu copiar o vetor e descobriu que as regras para descobrir quais são os 4 digitos da senha são as seguintes:

O primeiro digito está na posição da raiz quadrada da soma de todos os valores.
O segundo dígito esta na posição definida pelo o décimo primeiro valor impar do vetor multiplicado pelo antepenultimo valor par.
O terceiro dígito esta na posição resultante da soma do quadrado dos valores em posiçoes pares dividido pela metade da soma dos valores das posições impares.
O quarto dígito é a soma de todos os valores, e caso o resultado tenha mais de 1 dígito, soma-se novamente o resultado destes dígitos e assim sucessivamente até que reste apenas 1 dígito.
Escreva o programa para descobrir a senha do cofre. Considere que o vetor "Numeros" já esteja carregado.
"""

file = open('banco.txt')
numeros = []
for linha in file:
    for letra in linha:
        numeros.append(int(letra))
file.close()
print(len(numeros))

total = 0
for num in numeros:
    total += num
digito1 = numeros[int(total ** 0.5) - 1]

cont = 0
aux = 0
par = 0
impar = 0
while cont < 11:
    if numeros[aux] % 2 == 1:
        impar = num
        cont += 1
    aux += 1
aux = len(numeros) - 1
cont = 0
while cont < 3:
    if numeros[aux] % 2 == 0:
        par = num
        cont += 1
    aux -= 1
digito2 = numeros[par * impar - 1]

pares = 0
impares = 0
for i in range(len(numeros)):
    if i % 2 == 0:
        pares += numeros[i] ** 2
    else:
        impares += numeros[i]
digito3 = numeros[int(pares / (impares / 2)) - 1]

while total > 9:
    aux = str(total)
    total = 0
    for letra in aux:
        total += int(letra)
digito4 = total

print(digito1, digito2, digito3, digito4)
