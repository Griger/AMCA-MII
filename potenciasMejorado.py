'''
Metodo de las potencias normalizado sobre la matriz de Google
@author: Gustavo Rivas Gervilla
'''

'''
A continuacion se muestra la declaracion de las matrices de los dos casos de estudio como matrices de Numpy.
Caso 1: 

H = np.array([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1.0/3, 0.5, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0/3, 0],
[0, 0, 1.0/3, 0, 0, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5],
[1.0/3, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0],
[1.0/3, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0],
[1.0/3, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1.0/3, 0],
[0, 0, 0, 0.5, 0, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0, 0.5, 0, 1, 0, 0, 0, 0, 1.0/3, 0],
[0, 0, 0, 0, 0, 0, 1.0/3, 0, 0, 0, 0, 0.5, 0, 0.5],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]);



Caso 2: desaparecen las flechas A,B,C

H = np.array([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1.0/3, 0.5, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0/3, 0],
[0, 0, 1.0/3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5],
[1.0/3, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0],
[1.0/3, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0],
[1.0/3, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1.0/3, 0],
[0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0/3, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0.5],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]);
'''

import numpy as np

'''
Funcion que calcula la matriz A a partir de la H
@param H: la matriz de vinculos.
@return la matriz A calculada.
'''
def getA(H):
    #necesito saber que columnas tienen todos sus elementos nulos
    isNull = np.apply_along_axis(lambda col : not np.any(col != 0), 0, H)

    A = np.zeros(H.shape)

    #necesito contrarestar esas columnas con columnas con todos sus eltos. con valor 1/n
    A[:, isNull] = 1.0 / A.shape[1]

    return A
    

#H = np.array([[4,-1,1],[-1,3,-2],[1,-2,3]])

#declaro la matriz de vinculos
H = np.array([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1.0/3, 0.5, 0, 0.5, 0, 0, 0, 0, 0, 0, 1.0/3, 0],
[0, 0, 1.0/3, 0, 0, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5],
[1.0/3, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0],
[1.0/3, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0],
[1.0/3, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1.0/3, 0],
[0, 0, 0, 0.5, 0, 0, 1.0/3, 0, 0, 0, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0, 0.5, 0, 1, 0, 0, 0, 0, 1.0/3, 0],
[0, 0, 0, 0, 0, 0, 1.0/3, 0, 0, 0, 0, 0.5, 0, 0.5],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]);

#la matriz con todos sus elementos de la forma 1/n
aux = (1.0 / H.shape[0]) * np.ones(H.shape)

α = 0.85

S = H + getA(H)
G = α*S + (1 - α)*aux

#declaro el vector inicial para el metodo de las potencias
#v = np.array([1,0,0])
v = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

λs = []
vs = []

n = 200

#aplicamos el metodo de las potencias
for i in range(n):
    vPrev = v
    v = G.dot(v)

    notNullIdx = np.nonzero(vPrev)[0][0]

    λs.append(v[notNullIdx]/vPrev[notNullIdx])

    v = v / np.linalg.norm(v, ord = 1)
    vs.append(vPrev)

    
print(λs)
print(vs)
