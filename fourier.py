from sympy import integrate, summation, sin, cos, Symbol, pi, Piecewise, And, oo, Abs, Integer, simplify, Sum
from sympy.plotting import plot
import mpmath as mp

n,j,k = Symbol('n', integer = True), Symbol('j', integer = True), Symbol('k', integer = True)
t = Symbol('t')
psi = Piecewise((0, t < 0), (1, t < 0.5), (-1, t < 1), (0, True))

def an (f, n, p = pi):
    return integrate(f*cos(n*t*pi/p), (t, -p, p)) / p

def bn (f, n, p = pi):
    return integrate(f*sin(n*t*pi/p), (t, -p, p)) / p

def getFourierN (f, N, p = pi):
    return an(f, 0) + summation(an(f,n) * cos(n*t*pi/p), (n, 1, N)) + summation(bn(f, n) * sin(n*t*pi/p), (n, 1, N))

#Defino las funciones de los ejercicios

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

g = Piecewise((-t, t < 0), (t, 0 <= t), (0, True))

'''
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

H7 = getHaarN(g, 7)
H8 = getHaarN(g, 8)

p3 = plot(g, H7, H8, (t, -1, 1), show = False)
p3[0].line_color = 'red'
p3[0].line_color = 'blue'
p3[0].line_color = 'yellow'

print(H7)
#plot(H7, (t,0,1))
print(H7.subs(t,2).doit())
#p3.show()

#print(getFourierN(f, 6))
#getHaarN(g, 6)
#print(aux.subs(t, 0))

# Ejercicio 3

h = Piecewise((-6-t, And(-6 <= t, t < -3)), (t, And(-3 <= t, t < 3)), (6-t, And(3 <= t, t <= 6)))

# Ejercicio 4
