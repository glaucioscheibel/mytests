# π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
import math

pi = 0.0
op = 1

for i in range(1, 10000000, 2):
    pi += op * 4 / i
    op *= -1

print(pi)
print(math.pi)

