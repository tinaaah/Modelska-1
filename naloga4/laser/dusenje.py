import numpy as np
from scipy import integrate
import math

N = int(10e4)
time = np.linspace(0,100, N)
alpha = int(0.1)
r = 2
p = 0.125                                 #ali p res rabi bit manjsi od r

def deriv(X, t):
    A, F = X
    atomi = r - p*A*(F + 1)
    fotoni = F/p * (A - 1)
    return np.array([atomi, fotoni]) 

deltaa, deltaf=0.01, 0.01
#a0 = [r/p + deltaa, deltaf]            # začetni pogoji: okolica (r/p, 0)
#a0 = [1 + deltaa, r/p-1 + deltaf]      # začetni pogoji: okolica (1, r/p)

a0 = [2, 1.5]                             # preverim da res ne deluje za r<p
a, infodict = integrate.odeint(deriv, a0, time, full_output=True)
#infodict['message']
print('#r =', r, 'p =', p, sep='\t')
for i in range(len(a)):
    if i!=0 and i!= len(a)-1:
        if a[i][1] > a[i-1][1] and a[i][1] > a[i+1][1]:
            if abs(1-a[i][1])<0.01: break;
            print(a[i][1], time[i], sep = '\t')
print('')
#for i in range(len(a)):
    #print(a[i][0], a[i][1], time[i], sep='\t')
    #if a[i][0] < 1 or a[i][1] < 1:
        #break
#print('')
