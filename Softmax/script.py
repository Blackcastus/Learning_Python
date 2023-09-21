import numpy as np

def softmax(Z):
    # Z is a vector
    e_Z = np.exp(Z)
    A = e_Z / e_Z.sum(axis = 0)
    return A

def softmax_stable(Z):
    e_Z = np.exp(Z - np.max(Z, axis = 0, keepdims = True))
    A = e_Z / e_Z.sum(axis = 0)
    return A

v_z = [2, 1.8, 0]
a = softmax(v_z)
b = softmax_stable(v_z)

print(a)
print(b)