import numpy as np
from scipy import integrate
import math

time = np.linspace(0,21,num=1000)
mu, l = 0.01, 1

def deriv(x, t):                    #definicija odvoda
    A1, A2, B, C = x
    a1 = -A1**2 + mu*A1*A2
    a2 = A1**2 - mu*A1*A2 - l*mu*A2
    b = l * mu * A2
    c = l * mu * A2
    return np.array([a1, a2, b, c])

def prib(x, t):                    #definicija priblizka
    A1, B, C = x
    a1 = -l * A1**2 / (A1 + l)
    b = l * A1**2/(A1 + l)
    c = b
    return np.array([a1,b,c])

a0 = [1, 0, 0, 0]                #zacetne vrednosti vseh snovi
A = integrate.odeint(deriv, a0, time)
B = integrate.odeint(prib, [1,0,0], time)

for i in range(len(A)):
    a1 = B[i][0]
    a2 = a1**2 / (mu *(a1 + l))
    b = B[i][1]
    c = B[i][2]
    #print(-a1+A[i][0], -a2+A[i][1], -b+A[i][2], -c+A[i][3], time[i],sep='\t')
    #print(a1, a2, b, c, time[i],sep='\t')
    print(A[i][0], A[i][1], A[i][2], A[i][3], time[i],sep='\t')
print('')
