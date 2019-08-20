import numpy as np


Z = np.zeros((8,1),dtype=int)
Z[1::2]=1 # every 2 element, starting from index 1
print(Z)

Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)