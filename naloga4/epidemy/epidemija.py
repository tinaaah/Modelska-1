import numpy as np
from scipy import integrate
import math

time = np.linspace(0,100,num=1000)
alpha, beta = 0.5,0.05
def deriv(X, t):
    D = -alpha * X[0] * X[1]
    B = alpha * X[0] * X[1] - beta * X[1]
    I = beta * X[1]
    return np.array([D,B,I]) 

populacija = 1
start = 0.01
imuni = 0.5
start = [populacija - start - imuni,start,imuni] # začetni pogoji: dovzetni, bolani in imuni

a, infodict = integrate.odeint(deriv, start, time, full_output=True)
#infodict['message']
for i in range(len(a)):
    print(a[i][0], a[i][1], a[i][2], time[i], sep='\t')
    #if a[i][0] < 1 or a[i][1] < 1:
        #break
print('')
