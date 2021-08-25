import numpy as np
from scipy import integrate
import math

time = np.linspace(0,100,num=10000)
l = 10
def deriv(X, t):                    #definicija odvoda
    x, y, z, w = X
    t1 = - 2*x*w + 2*l*z*y
    t2 = x*w - l*z*y
    t3 = - 2*l*z*y
    t4 = - x*w 
    return np.array([t1,t2,t3,t4])

epsilon = 1e-4
#a0 = [epsilon, epsilon, epsilon, 1-3*epsilon, 1]    #zacetne vrednosti vseh snovi
a0 = [1, 0, 0.8*0.5, 0.5]

A = integrate.odeint(deriv, a0, time)

for i in range(len(A)):
    print(A[i][0], A[i][1], A[i][2], A[i][3], time[i], sep='\t')
print('')
