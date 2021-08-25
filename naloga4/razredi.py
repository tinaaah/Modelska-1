import numpy as np
from scipy import integrate
import math

"""Razdelimo obolele na vec razredov"""

time = np.linspace(0,180,num=1000)
alpha, beta1, beta2, beta3, beta4, beta5, beta6 = 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1
def deriv(X, t):
    D = -alpha*X[0] * X[1]
    B1 = alpha*X[0] * X[1] - beta1*X[1]
    B2 = beta1*X[1] - beta2*X[2]
    B3 = beta2*X[2] - beta3*X[3]
    B4 = beta3*X[3] - beta4*X[4]
    B5 = beta4*X[4] - beta5*X[5]
    B6 = beta5*X[5] - beta6*X[6]
    I = beta6*X[6]
    return np.array([D,B1,B2,B3,B4,B5,B6,I]) 

populacija = 1
start = 1e-6
start = [populacija - 6*start, start, start, start, start, start, start, 0] 

a, infodict = integrate.odeint(deriv, start, time, full_output=True)
#infodict['message']
for i in range(len(a)):
    print(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7], time[i], sep='\t')
    #if a[i][0] < 1 or a[i][1] < 1:
        #break
