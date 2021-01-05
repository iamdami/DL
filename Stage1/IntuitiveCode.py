import numpy as np

a = np.random.randn(5, 1)
print(a)
print()

print(a.T)  # a transpose becomes row vector
print()

print(np.dot(a, a.T))  # dot product of a transpose and a
print()
