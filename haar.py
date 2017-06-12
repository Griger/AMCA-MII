from sympy import integrate, summation, sin, cos, Symbol, pi, Piecewise, And, oo, Abs, Integer, simplify, Sum, Integral
from sympy.plotting import plot
import mpmath as mp

n,j,k = Symbol('n', integer = True), Symbol('j', integer = True), Symbol('k', integer = True)
t = Symbol('t')
psi = Piecewise((0, t < 0), (1, t < 0.5), (-1, t < 1), (0, True))

'''Funcion que obtiene el aproximante de Haar j,k'''
def getHaarAprox (jj,kk):
    return (2**(jj/2)) * psi.subs(t, 2**jj * t - kk)

'''Funcion que obtiene el coeficiente j,k para la serie de Haar para la funcion f'''
def ajk (f, jj, kk):
    
    if kk <= 2**jj -1:
        return Integral(f * getHaarAprox(jj,kk), (t,0,1)).evalf(maxn = 10)
    else:
        return 0
    #return Integral(f * getHaarAprox(jj,kk), (t,0,1)).evalf(maxn = 10)

'''Funcion que obtiene la serie de Haar hasta el termino N-esimo'''
def getHaarN (f, N):
    return mp.nsum(lambda j,k : ajk(f,j,k) * getHaarAprox(j,k), [0,N], [0,N])
    #return summation(ajk(f,j,k) * getHaarAprox(j,k), (k, 0, 2**j - 1), (j, 0, N))

#Ejercicio 2

g = Piecewise( (-t, t < 0), (t, t >= 0) )

H8 = getHaarN(g,8)
H10 = getHaarN(g,10)
H12 = getHaarN(g,5)

p1 = plot(g, H8, H10, H12, (t, 0, 1), show = False)
p1[0].line_color = 'red'
p1[1].line_color = 'blue'
p1[2].line_color = 'green'
p1[3].line_color = 'yellow'

p1.show()

#Ejercicio 4

'''
h = Piecewise((-6-t, t < -3), (t, t < 3), (6-t, t <= 6))
h = h.subs(t, 12*t - 6)

H8 = getHaarN(h,8)
H10 = getHaarN(h,10)
H12 = getHaarN(h,12)

p2 = plot(h, H8, H10, H12, (t, 0, 1), show = False)
p2[0].line_color = 'red'
p2[1].line_color = 'blue'
p2[2].line_color = 'green'
p2[3].line_color = 'yellow'

p2.show()
'''
