import numpy as np
from numpy import linalg as LA
from scipy.optimize import minimize
import math
import random
import timeit

random.seed()
N = 30-1 #Definiram stevilo nabojev, s tem da je en fiksen
k = 1 #4*pi*epsilon_0
sin = math.sin
cos = math.cos
pi = math.pi
sqrt = math.sqrt

fi = [2*pi*random.uniform(0,1) for _ in range(N)]
theta = [pi*random.uniform(0,1) for _ in range(N)]
koti = np.concatenate((fi, theta))
#print(koti)

n =[]
en = []

def E(x):
    W = 0
    n = N
    for i in range(-1, n):
        if i == -1:
            fi1, theta1 = 0,0
        else: 
            fi1, theta1 = x[i], x[i+n]

        for j in range(i+1,n): 
            fi2, theta2 = x[j], x[j+n] 
            difx = cos(fi1)*sin(theta1) - cos(fi2)*sin(theta2) 
            dify = sin(fi1)*sin(theta1) - sin(fi2)*sin(theta2) 
            difz = cos(theta1) - cos(theta2) 
            norma = sqrt(difx**2 + dify**2 + difz**2) 
            W += 1/norma
    en.append(W)
    #print(W)
    return(W)

start = timeit.default_timer()

result = minimize(fun=E, x0=koti, method='Powell')
angle = result.x
print((N+1),result.fun, sep='\t')

stop = timeit.default_timer()
#print('#N \t\t Cas')
#print('Cas:', stop-start, sep='\t')
#print(N+1,stop - start, sep='\t')


r = []
r.append([0,0,1])

#print(0,0,1,sep='\t')
"""
for i in range(N):
    fi, theta = angle[i], angle[i+N]
    x = cos(fi) * sin(theta) 
    y = sin(fi) * sin(theta) 
    z = cos(theta) 
    r.append([x,y,z])
    #print(x,y,z,sep='\t')
"""

#print(en)
#p = np.sum(r, axis=0)
#p=LA.norm(r)

#print(N+1,LA.norm(p),sep='\t')

#b = [0,R]
#B = tuple(map(tuple,np.vstack([b]*3)))
