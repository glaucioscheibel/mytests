def hanoi(n, o, d, t):
    if n > 0:
        hanoi(n - 1, o, t, d)
        print(f'{o} -> {d}')
        hanoi(n - 1, t, d, o)


hanoi(12, 'A', 'B', 'C')
