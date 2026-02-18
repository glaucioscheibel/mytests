"""
Faça um programa que encontre o conjunto de 5 dígitos consecutivos na conjunto de valores do arquivo numeros.txt que gere o maior produto:
"""
numeros = ''
arquivo = open('AchaProduto/numeros.txt')
for linha in arquivo:
    numeros += linha
print(numeros)

maiorNumero = ''
maiorProduto = 0

for i in range(len(numeros) - 4):
    produto = 1
    numero = ''
    for j in range(i, i + 5):
        numero += numeros[j]
        produto *= int(numeros[j])
    if produto > maiorProduto:
        maiorNumero = numero
        maiorProduto = produto
    print(produto)
print(maiorNumero, 'tem o produdo', maiorProduto)