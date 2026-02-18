"""
Dadas duas sequências com n números inteiros entre 0 e 9, interpretadas como dois números inteiros de n algarismos, calcular a sequência de números que representa a soma dos dois inteiros.

    1  8  2  4  3  4  2  5  1
+      3  3  7  5  2  3  3  7
    -------------------------
    2  1  6  1  8  6  5  8  8
"""
# Entrada
num1 = input("Num1: ")
num2 = input("Num2: ")

v1 = []
v2 = []

for digito in num1:
    v1.append(int(digito))
for digito in num2:
    v2.append(int(digito))

# Deixa os dois com o mesmo tamanho
while len(v1) < len(v2):
    v1.insert(0, 0)
while len(v2) < len(v1):
    v2.insert(0, 0)

total = []
sobra = 0

# Faz as somas
for i in range(len(v1) - 1, -1, -1):
    aux = v1[i] + v2[i] + sobra
    if aux > 9:
        aux = aux % 10
        sobra = 1
    else:
        sobra = 0
    total.insert(0, aux)
if sobra != 0:
    total.insert(0, sobra)

# Saída
print(v1)
print(v2)

print(total)