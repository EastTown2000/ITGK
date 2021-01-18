import numpy as np
def add_matrix(a,b):
  length = len(a)
  c = []
  for i in range(length):
    a_np = np.array(a[i])
    b_np = np.array(b[i])
    c.append(list(a_np + b_np))
  return c

a = [[1,2,3,4,5], [6,7,8,9,0]]
b = [[1,3,5,7,9], [2,4,6,8,0]]
print(add_matrix(a,b))