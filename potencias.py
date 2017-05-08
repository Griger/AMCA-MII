'''
Metodo de las potencias normalizado
@author: Gustavo Rivas Gervilla
'''

import numpy as np

A = np.array([[4,-1,1],[-1,3,-2],[1,-2,3]])
v = np.array([1,0,0])
λs = []
vs = []

n = 200

for i in range(n):
    vPrev = v
    v = A.dot(v)

    notNullIdx = np.nonzero(vPrev)[0][0]

    λs.append(v[notNullIdx]/vPrev[notNullIdx])

    v = v / np.linalg.norm(v, ord = 1)
    vs.append(vPrev)

    
print(λs)
print(vs)
