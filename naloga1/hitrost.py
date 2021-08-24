import numpy as np
from decimal import *
import math
from pylab import *
import sys
import Gnuplot
from scipy import special
import time

def F(k,x):
    return special.gamma(1/3+k)/special.gamma(1/3) * 3**k * x**(3*k)/ math.factorial(3*k)
def G(k,x):
    return special.gamma(2/3+k)/special.gamma(2/3) * 3**k * x**(3*k+1)/ math.factorial(3*k+1)

a=0.355028053887817239
b=0.258819403792806798

def taylorA(x):
    A=0 
    for i in range(50):
        A += a*F(i,x) - b*G(i,x)
    return A
def taylorB(x):
    B=0
    for i in range(50):
        B += (a*F(i,x) + b*G(i,x))* math.sqrt(3)
    return B

def u_s(x,s):
    temp = 1
    if(s==0): return 1
    for i in range(s,3*s): 
        temp*=(i+1/2)
    for i in range(1,s+1): 
        temp/= 54*i*x
    return temp

def L(x):
    nov = 1
    zadnji = nov 
    vsota = 1
    eps = 10e-20
    i = 1
    while math.fabs(zadnji) > eps:
        nov =  u_s(x,i)
        if math.fabs(nov) > math.fabs(zadnji):
            break
        else:
            vsota += nov
            zadnji = nov
        i += 1
    return vsota

def P(x):
    nov = 1
    zadnji = nov
    vsota = 1
    eps = 10e-15
    i = 1
    while math.fabs(zadnji) > eps:
        nov =  (-1)**i *  u_s(x,2*i)
        if math.fabs(nov) > math.fabs(zadnji):
            break
        else:
            vsota += nov
            zadnji = nov
        i +=1
    return vsota

def Q(x):
    nov = 5/(72*x)
    zadnji = nov
    vsota = zadnji
    eps = 10e-15
    i = 1
    while math.fabs(zadnji) > eps:
        nov = (-1)**i * u_s(x,2*i+1) 
        if math.fabs(nov) > math.fabs(zadnji):
            break
        else:
            vsota += nov
            zadnji = nov
        i+=1
    return vsota
def zeta(x):
    return math.pow(math.fabs(x),3.0/2)*2/3

def pozA(x): 
    return np.exp(-zeta(x))*L(-zeta(x)) / (2*math.sqrt(math.pi)*x**(1/4))

def pozB(x):
    return np.exp(zeta(x))*L(zeta(x))/(math.sqrt(math.pi)*x**(1/4))

def negA(x):
    sinus = math.sin(zeta(x)-math.pi/4)
    kosinus = math.cos(zeta(x)-math.pi/4)
    return (sinus*Q(zeta(x)) + kosinus*P(zeta(x))) / (math.sqrt(math.pi)*(-x)**(1/4))

def negB(x):
    sinus = math.sin(zeta(x)-math.pi/4)
    kosinus = math.cos(zeta(x)-math.pi/4)
    return (-sinus*P(zeta(x)) + kosinus*Q(zeta(x))) / (math.sqrt(math.pi)*(-x)**(1/4))

def f(x):
    return math.pow(x,2./3) * ( 1 + 5/48*math.pow(x,-2) - 5/36*math.pow(x,-4) + 77125/82944*math.pow(x,-6) -108056875/6967293*math.pow(x,-8))
def a(s):
    return -f(3*math.pi*(4*s-1)/8)
def b(s):
    return -f(3*math.pi*(4*s-3)/8)
print(a(100))
g=Gnuplot.Gnuplot()
g("set term epslatex colour solid rounded noheader")
g("set out 'proba.tex'")

g("set key right top reverse samplen 1 width 1 height .5")

g.title("Negativna os")

g("set grid lc -1 lw .5")
g("set logscale y")

os = np.arange(start=-100, stop=-1, step=5e-3, dtype='float_')
y=special.airy(os)

tempA = np.vectorize(negA)
tempB = np.vectorize(negB)
Ai = tempA(os)
Bi = tempB(os)

count=0
for i in range(len(Ai)-1,0,-1):
    if fabs(Ai[i]) <= 3.3e-3:
#        print(os[i],Ai[i],sep='\t')
        count+=1
    if count==100:
        break

print(count,Ai[i],os[i])


n=0
diferencA=[]
diferencB=[]
for i in range(len(os)):
    if math.fabs(1-(Ai[i]/y[0][i])) >= 10e-10:
        n+=1
        #print((Ai[i]-y[0][i])/y[0][i], '\t', os[i])
    diferencA.append(math.fabs(1-(Ai[i]/y[0][i])))
    diferencB.append(math.fabs((Bi[i]-y[2][i])/y[2][i]))
#print(n,'\t',len(os))
#print(max(diferencA))

#for i in range(len(os)):
#    print(os[i],Ai[i],Bi[i],diferencA[i],diferencB[i],sep='\t')


"""
d1=Gnuplot.Data(os,Ai, title="napaka A", with_="lines")
d2=Gnuplot.Data(os,y[0], title="napaka B", with_="lines")

g.plot(d2)
"""

g("unset term")
g("set term dumb")
g("unset out")
g("set out '/dev/null'")

del g
