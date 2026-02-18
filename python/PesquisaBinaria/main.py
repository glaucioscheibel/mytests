"""
Peça para o usuário informar um número entre 1 e 250000, e informe a ele em qual posição o número encontra-se no vetor.
https://repl.it/@gscheibel/PesquisaBinaria
"""
nums = []

for i in range(1, 1001):
    if i % 5 != 0:
        nums.append(i)
print(len(nums))
# Algoritmo da Pesquisa Binária:
num = int(input('Informe o número a ser localizado: '))
ini = 0
fim = len(nums) - 1
achou = False
while not achou and ini <= fim:
    meio = int((ini + fim) / 2)
    print(ini, fim, meio, nums[meio])
    if nums[meio] == num:
        achou = True
    elif nums[meio] < num:
        ini = meio + 1
    else:
        fim = meio - 1
if achou:
    print('numero:' , nums[meio], ' posicao: ', meio)  
else:
    print('O número', num, 'non ecziste!')
