import numpy as np
from scipy import integrate
import math

"""Razdelimo obolele na vec razredov"""

time = np.linspace(0,250,num=1000)
alpha, beta1, beta2, beta3, beta4, beta5, beta6 = 0.5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1
#alpha, beta = 0.5, 0.1
def deriv(X, t):
    B = sum(X[1:-1])
    D = -alpha*X[0] * B
    B1 = alpha*X[0] * B - beta1*X[1]
    B2 = beta1*X[1] - beta2*X[2]
    B3 = beta2*X[2] - beta3*X[3]
    B4 = beta3*X[3] - beta4*X[4]
    B5 = beta4*X[4] - beta5*X[5]
    B6 = beta5*X[5] - beta6*X[6]

    B7 = beta5*X[6] - beta6*X[7]
    B8 = beta5*X[7] - beta6*X[8]
    B9 = beta5*X[8] - beta6*X[9]
    B10 = beta5*X[9] - beta6*X[10]
    B11 = beta5*X[10] - beta6*X[11]
    B12 = beta5*X[11] - beta6*X[12]
    I = beta6*X[12]
    #return np.array([D,B1,B2,B3,B4,B5,B6,I]) 
    return np.array([D,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,I]) 
    #return np.array([D,B1,B2,B3,I]) 

populacija = 1
start = 1e-6
#start = [populacija - 6*start, start, start, start, start, start, start, 0] 
#start = [populacija - 3*start, start, start, start, 0] 
start = [populacija - 12*start, start, 0, 0,0,0,0,0,0,0,0,0,0, 0] 

a, infodict = integrate.odeint(deriv, start, time, full_output=True)
#infodict['message']
for i in range(len(a)):
    #print(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7], time[i], sep='\t')
    print(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7], a[i][8],
            a[i][9], a[i][10], a[i][11], a[i][12],a[i][13],time[i], sep='\t')
    #print(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], time[i], sep='\t')
    #if a[i][0] < 1 or a[i][1] < 1:
        #break
