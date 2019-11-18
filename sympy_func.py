import sympy as sym
from math import *
x = sym.Symbol('x')
t= sym.Symbol('t')
print(sym.diff(x**5))
b=1
a=0
x = sym.expand((b-a)/2*t)
exp = x.expand()
print(exp)
print(exp.subs(t,1))