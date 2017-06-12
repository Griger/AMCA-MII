from sympy import integrate, summation, sin, cos, Symbol, pi, Piecewise, And, oo, Abs, Integer, simplify, Sum
from sympy.plotting import plot
import mpmath as mp

n,j,k = Symbol('n', integer = True), Symbol('j', integer = True), Symbol('k', integer = True)
t = Symbol('t')
psi = Piecewise((0, t < 0), (1, t < 0.5), (-1, t < 1), (0, True))

'''Funcion que obtiene el termino an de la serie de Fourier para f
:param p: El extremos superior del intervalo en el que definimos la funcion, [-p,p]
'''
def an (f, n, p = pi):
    return integrate(f*cos(n*t*pi/p), (t, -p, p)) / p

'''Funcion que obtiene el termino bn de la serie de Fourier para f
:param p: El extremos superior del intervalo en el que definimos la funcion, [-p,p]
'''
def bn (f, n, p = pi):
    return integrate(f*sin(n*t*pi/p), (t, -p, p)) / p

'''Funcion que obtiene la serie de Fourier para f hasta el termino N-esimo.
:param p: El extremos superior del intervalo en el que definimos la funcion, [-p,p]
'''
def getFourierN (f, N, p = pi):
    return an(f, 0,p)/2 + summation(an(f,n,p) * cos(n*t*pi/p), (n, 1, N)) + summation(bn(f, n,p) * sin(n*t*pi/p), (n, 1, N))

# Ejercicio 1

'''
f = Piecewise((-1, t < 0), (1, t > 0), (0, True))
S6 = getFourierN(f, 6)
S7 = getFourierN(f, 7)
S8 = getFourierN(f, 8)

p1 = plot(f, S6, S7, S8, (t, -pi, pi), legend = True, show = False)
p1[0].line_color = 'red'
p1[1].line_color = 'blue'
p1[2].line_color = 'green'
p1[3].line_color = 'yellow'

p1.show()
'''

# Ejercicio 2

'''
g = Piecewise((-t, t < 0), (t, 0 <= t), (0, True))

S6 = getFourierN(g, 6)
S7 = getFourierN(g, 7)
S8 = getFourierN(g, 8)

p2 = plot(g, S6, S7, S8, (t, -pi, pi), legend = True, show = False)
p2[0].line_color = 'red'
p2[1].line_color = 'blue'
p2[2].line_color = 'green'
p2[3].line_color = 'yellow'

p2.show()
'''

# Ejercicio 3

h = Piecewise((-6-t, t < -3), (t, t < 3), (6-t, t <= 6))

S6 = getFourierN(h, 6, 6)
S7 = getFourierN(h, 7, 6)
S8 = getFourierN(h, 8, 6)

p3 = plot(h, S6, S7, S8, (t, -6, 6), legend = True, show = False)
p3[0].line_color = 'red'
p3[1].line_color = 'blue'
p3[2].line_color = 'green'
p3[3].line_color = 'yellow'

p3.show()
