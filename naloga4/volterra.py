import numpy as np
from scipy import integrate
import math

time = np.linspace(0,15,num=1000)
a, b, c, d = 1, 0.1, 1.5, 0.75
def deriv(X, t):
    x0 = (X[0])
    x1 = (X[1])
    return np.array([ a*x0 -   b*x0*x1, -c*x1 + d*b*x0*x1 ])

a0 = [50,50]              # začetni pogoji: 10 zajcev in 5  lisic

a, infodict = integrate.odeint(deriv, a0, time, full_output=True)
#infodict['message']
for i in range(len(a)):
    print(int(a[i][0]), int(a[i][1]), time[i], sep='\t')
    #if a[i][0] < 1 or a[i][1] < 1:
        #break
