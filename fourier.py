from sympy import integrate, summation, sin, cos, Symbol, pi, Piecewise, And, oo, Abs, Integer, simplify, Sum

π = pi
n, j, k = Symbol('n', integer = True), Symbol('j', integer = True), Symbol('k', integer = True)
t = Symbol('t')
ψ = Piecewise((1, And(0 <= t, t < 0.5)), (-1, And(0.5 <= t, t < 1)), (0, True))

def an (f, n, p = π):
    return integrate(f*cos(n*t*π/p), (t, -p, p)) / p

def bn (f, n, p = π):
    return integrate(f*sin(n*t*π/p), (t, -p, p)) / p

def getFourierN (f, N, p = π):
    return an(f, 0) + summation(an(f,n) * cos(n*t*π/p), (n, 1, N)) + summation(bn(f, n) * sin(n*t*π/p), (n, 1, N))

def getHaarAprox (j,k):
    return (2**(j/2)) * ψ.subs(t, 2**j * t - k)

def ajk (f, j, k):
    return integrate(f * getHaarAprox(j,k), (t, 0, 1))

def getHaarN (f, N):
    return summation(ajk(f,j,k) * getHaarAprox(j,k), (k, 0, 2**j - 1), (j, 0, N))
    
 # Defino las funciones de los ejercicios

f = Piecewise((-1, And(-pi < t, t < 0)), (1, And(0 < t, t < pi)), (0, True))
#g = Piecewise((-t, And(-π < t, t < 0)), (t, And(0 <= t, t < π)), (0, True))
g = Abs(t)
h = Piecewise((-6-t, And(-6 <= t, t < -3)), (t, And(-3 <= t, t < 3)), (6-t, And(3 <= t, t <= 6)))

# Ejercicio 1

#print(getFourierN(f, 6))

# Ejercicio 2

#print(getFourierN(f, 6))
aux = getHaarN(g, 6)
print(aux.subs(t, 0))

# Ejercicio 3
# Ejercicio 4
