import numpy as np
from scipy.stats import linregress
import math

tab = np.loadtxt('CdL3_linfit.norm', usecols=range(0,5))
energija,y1,y2,A = [], [], [], []
for i in range(len(tab)):
    energija.append(tab[i][0])
    y1.append(tab[i][1])
    y2.append(tab[i][2])
    A.append([tab[i][3],tab[i][4]])

energija,y1,y2,A = np.matrix(energija), np.matrix(y1), np.matrix(y2), np.matrix(A)

U, D, V = np.linalg.svd(A, full_matrices=False)
#print(U.shape,D.shape,V.shape)
S = np.diag(D)
X_a = np.matmul(np.matmul(U, np.diag(D)), V)
#print(np.std(A), np.std(X_a), np.std(A - X_a))

#----------------------------------------------------- izracunamo ven fite

x1, x2 = 0,0
#print(y1)
#print( np.dot(U[:,0].T, y1.T ))
#print(U)
for i in range(2):
    x1 += np.dot(np.dot(U[:,i].T, y1.T), V[i,:]) / S[i,i]
    x2 += np.dot(np.dot(U[:,i].T, y2.T), V[i,:]) / S[i,i]
print(x1)
print(x2)

#----------------------------------------------------- rcunam se varianco x-ov

M =[]
k = 0
for j in range(2):
    for i in range(2):
        #print(i,j,k)
        M.append(V[i,j]*V[i,k]/ S[i,i]**2)
    k += 1
print(M)
