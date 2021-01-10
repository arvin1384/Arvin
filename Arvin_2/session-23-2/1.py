import numpy as np


a = np.arange(15).reshape(3,5)
print(a)
print(type(a))

print(f"Dimentions: {a.ndim}")
print(f"Data types inside: {a.dtype.name}")
print(f"Size of a array: {a.size}")
