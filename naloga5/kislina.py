import numpy as np
from scipy import integrate
import math

time = np.linspace(0,100,num=10000)

m = 2.5
r = 1
p = 100
def deriv(X, t):                    #definicija odvoda
    x, y, z = X
    p1 = y*math.sqrt(z)/(m + x/z)
    p2 = -1/2*y*math.sqrt(z)/(m + x/z)
    p3 = -1/2*y*math.sqrt(z)/(m + x/z)
    return np.array([p1, p2, p3])

#celota = 1
b = 1
h = r * b
hi = p * b

a0 = [hi, b, h]                #zacetne vrednosti vseh snovi

A = integrate.odeint(deriv, a0, time)

for i in range(len(A)):
    print(A[i][0], A[i][1], A[i][2], time[i], sep='\t')
print('')
