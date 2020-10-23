import numpy as np

def areOrthogonal(a,b):
    vek_1 = np.array(a)
    vek_2 = np.array(b)
    return np.dot(vek_1,vek_2) == 0

vk_1 = [1,2]
vk_2 = [-2,1]
print(areOrthogonal(vk_1,vk_2))