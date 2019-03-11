import numpy as np

z = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

a = np.reshape(z, (-1,2,2))
print(a)
