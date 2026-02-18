"""
Euler = 1/0! + 1/1! + ... + 1/n!
"""

euler = 0

for n in range(30):
    fat = 1
    for x in range(1, n + 1):
        fat *= x
    euler += (1 / fat)

print(euler)
