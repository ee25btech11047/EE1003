import numpy as np

h = 0.001
x = np.arange(0, 3+h, h)

total = 0

for xi in x:
    y = np.arange(0, 3 - xi + h, h)
    for yj in y:
        total += (6 - xi - yj)

result = total * h * h
print(result)
