import numpy as np
from scipy.stats import linregress
import math

tab = np.loadtxt('farmakoloski.dat', usecols=range(0,2))
L=len(tab)
sigma = 3
z,t,napake = [],[],[]

for i in range(L):
    x = tab[i][0]
    y = tab[i][1]
    t.append(1/x)
    z.append(1/y)
    napake.append(sigma/y**2)

X = [t,z,napake]
P, D, Q = np.linalg.svd(X, full_matrices=False)
X_a = np.matmul(np.matmul(P, np.diag(D)), Q)
#print(np.std(X), np.std(X_a), np.std(X - X_a))

def hi(X):
    t,z,napaka = X

    for i in range(L):
        A11 += 1/napaka[i]**2
        A12 += 1/napaka[i]**2 * t[i]
        A22 += 1/napaka[i]**2 * t[i]**2
        b1 += 1/z[i] * 1/napaka[i]**2
        b2 += 1/z[i] * 1/napaka[i]**2 * t[i]
    return [[[A11,A12],[A12,A22]],[b1,b2]]
A,b=hi([t,z,napake])
print(A,b,sep='\n\n')
a = np.matmul(A,b)
print(a)

