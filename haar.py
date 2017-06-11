from sympy import integrate, summation, sin, cos, Symbol, pi, Piecewise, And, oo, Abs, Integer, simplify, Sum, Integral
from sympy.plotting import plot
import mpmath as mp

n,j,k = Symbol('n', integer = True), Symbol('j', integer = True), Symbol('k', integer = True)
t = Symbol('t')
psi = Piecewise((0, t < 0), (1, t < 0.5), (-1, t < 1), (0, True))

def getHaarAprox (jj,kk):
    return (2**(jj/2)) * psi.subs(t, 2**jj * t - kk)

def ajk (f, jj, kk):
    
    if kk <= 2**jj -1:
        return Integral(f * getHaarAprox(jj,kk), (t,0,1)).evalf(maxn = 10)
    else:
        return 0
    #return Integral(f * getHaarAprox(jj,kk), (t,0,1)).evalf(maxn = 10)
    
def getHaarN (f, N):
    return mp.nsum(lambda j,k : ajk(f,j,k) * getHaarAprox(j,k), [0,N], [0,N])
    #return summation(ajk(f,j,k) * getHaarAprox(j,k), (k, 0, 2**j - 1), (j, 0, N))

g = Piecewise( (-t, t < 0), (t, t >= 0) )

H0 = getHaarN(g,0)
H2 = getHaarN(g,0)
H4 = getHaarN(g,0)

p1 = plot(g, H0, H2, H4, (t, 0, 1), show = False)
p1[0].line_color = 'red'
p1[1].line_color = 'blue'
p1[2].line_color = 'green'
p1[3].line_color = 'yellow'

p1.show()

