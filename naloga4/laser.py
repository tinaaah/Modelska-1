import numpy as np
from scipy import integrate
import math

time = np.linspace(0,20,num=5000)
r = 5
p = 4*r/(r**2+4)

def deriv(X, t):
    A, F = X
    atomi = r - p*A*(F + 1)
    fotoni = F/p * (A - 1)
    return np.array([atomi, fotoni]) 

deltaa, deltaf=0.3, 0.3
#a0 = [r/p + deltaa, deltaf]            # začetni pogoji: okolica (r/p, 0)
a0 = [1 + deltaa, r/p-1 + deltaf]       # začetni pogoji: okolica (1. r/p)

a, infodict = integrate.odeint(deriv, a0, time, full_output=True)
#infodict['message']
#for i in range(len(a)):
#    print(a[i][0], a[i][1], time[i], sep='\t')
    #if a[i][0] < 1 or a[i][1] < 1:
        #break
print('')
