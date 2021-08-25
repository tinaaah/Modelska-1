import numpy as np
from numpy import linalg as LA
from scipy.optimize import minimize
import math
import random
import timeit


random.seed()
exp = math.exp

N = 50-2            #stevilo vseh hitrosti
deltay = 1/(N+1)    #dolzina intervala
xi = 10              #zatolce dol eksponent
alpha = 5           #za omejitev hitrosti
beta = 10            #za omejitev pospeska

v0 = 2.0             #zacetna hitrost
vn = v0              #koncna hitrost
v_max = 2         #maks hitrost

def F(x): 
    F0 = 0
    F2 = 0
    F3 = 0
    V = 1/2 * (v0+vn)
    for i in range(N): 
        if i == 0: 
            a = 1/2
            x0 = v0
            x1 = x[i]
        elif i==N-1: 
            #dx = 1/2 * ((x[i] - x[i-1])/deltay)**2
            a = 1/2
            x0 = x[i-1]
            x1 = x[i]
        else: 
            a = 1
            x0 = x[i-1]
            x1 = x[i]
        F0 += a*(x1 - x0)**2
        V += a*x1
        F2 += exp(-beta*x1)
        F3 += exp(-beta*(x1 - v_max))
    F0 += a*(x1 - vn)**2
    V += a*vn
    F1 = exp(xi*(V - 1/deltay))
    F2 += exp(-beta*vn)
    F3 += exp(-beta*(vn - v_max))
    return F0+F1+F2+F3
def multiplikator(x):
    
    return Lambda*(V-1)

cons = [{'type':'ineq', 'fun': lambda x: x},]

#start = timeit.default_timer()

v_0 = [random.uniform(0,1) for _ in range(N)]

#result = minimize(fun=F, x0=v_0, constraints=cons) 
result = minimize(fun=F, x0=v_0, method='BFGS')
resitev = np.r_[v0, np.array(result.x), vn]
#resitev = np.r_[v0,np.array(result.x),vn]
#print(resitev)

#stop = timeit.default_timer()

for i in range(len(resitev)):
    print(i/(N+1), resitev[i], sep='\t')

