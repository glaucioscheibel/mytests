v = [9, 2, 3, 6, 5, 4, 7, 8, 1]

for i in range(1, len(v)):
    chave = v[i]
    j = i - 1
    while j >= 0 and v[j] > chave:
        v[j + 1] = v[j]
        j = j - 1
        v[j + 1] = chave

print(v)
