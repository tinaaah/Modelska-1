import numpy as np
from scipy.stats import linregress
import math

tab = np.loadtxt('farmakoloski.dat', usecols=range(0,2))
L=len(tab)
sigma = 3

#------------------------------------------------- Najprej nardim hi**2 metodo
z,t,napake = [],[],[]
A11,A12,A22,b1,b2 = 0,0,0,0,0
x,y,X,Y = [],[],[],[]

for i in range(L):
    x.append(tab[i][0])
    y.append(tab[i][1])
    X.append(1/x[i])
    Y.append(1/y[i])
    napaka = sigma/y[i]**2
    A11 += 1/napaka**2
    A12 += 1/(napaka**2 * x[i])
    A22 += 1/(napaka**2 * x[i]**2)
    b1 += 1/(y[i]*napaka**2)
    b2 += 1/(y[i]*napaka**2*x[i])

#------------------------------------------------------ Navadna regresija brez napak
slope, intercept, r_value, p_value, std_err = linregress(X,Y)
w = 1/intercept
c = slope*w

#------------------------------------------------------ sprintam vse vrednosti in hi**2
A = np.matrix( [[A11,A12],[A12,A22]] )

inverz = A.I
b = np.matrix([[b1],[b2]])
a = np.matmul(inverz,b)

n = np.matrix.item(a[0][0])
k = np.matrix.item(a[1][0])

y0 = 1/n
b = k*y0

T1,T2=0,0
for i in range(L):
    delta1 = y[i] - ( y0*x[i] / (x[i] + b) )
    delta2 = y[i] - ( w*x[i] / (x[i] + c) )
    T1 += ((y[i] - ( y0*x[i] / (x[i] + b) ))/sigma)**2
    T2 += ((y[i] - ( w*x[i] / (x[i] + c) ))/sigma)**2
    print(abs(delta1)/y[i], abs(delta2)/y[i], x[i], sep='\t')

#----------------------------------------------------- Naredimo še singularni razcep

#X = [t,z,napake]
#P, D, Q = np.linalg.svd(X, full_matrices=False)
#X_a = np.matmul(np.matmul(P, np.diag(D)), Q)
#print(np.std(X), np.std(X_a), np.std(X - X_a))
