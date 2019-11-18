import sympy as sym
from math import *
x = sym.Symbol('x')
y = sym.Symbol('y')
t = sym.Symbol('t')
dx = sym.Symbol('dx')
dt = sym.Symbol('dt')
#def fun(t):
   ## return 1/(1+(x.expand()))

def fx():
    #print(t)
    ##dx = sys.diff(2*x*)
    #(sym.diff(x.expand(),t)
    return 1/(1+(x.expand()) ) *sym.diff(x.expand())

def onepoint():
    #sys.diff()
    return 2*fx().subs(t,0)

def twopoint():
    return (fx().subs(t,1/sqrt(3))+fx().subs(t,(-1/sqrt(3))))

def threepoint():
    return (5*fx().subs(t,(-sqrt(3/5)))+8*fx().subs(t,0)+5*fx().subs(t,(sqrt(3/5))))/9
#t = 0
funx = input("Enter f(x) : ")
b = int(input("Enter Upper limit of f(x) : "))
a = int(input("Enter Lower limit of f(x) : "))
if b!=1 or a !=- 1:
    x = sym.expand((((b-a)/2)*t+(b+a)/2))
    #print(fx().subs(t,(-sqrt(3/5))))
    print(onepoint())
    print(twopoint())
    print(threepoint())
    #print(fun(0))
    #t=0
    #print(onepoint().subs(t,0))
    #twopoint()
    #print(threepoint())
    #print(x.expand())
    #print(sym.diff(x.expand()))
    #print(fx(0))

else:
    x = t
    print(fx().subs(t,0))




#print(x)
#print(x.expand())

#sys.subs(x)
#print(f())
#print(t.expand())

