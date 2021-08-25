import numpy as np
from scipy.stats import linregress
import math
from scipy.stats import chisquare

tab = np.loadtxt('thtg-xfp-thfp.dat', usecols=range(0,3))
L=len(tab)
x = tab[:,1]
theta1 = tab[:,2]
theta2 = tab[:,0]

theta1 = math.pi/180*theta1*1000
theta2 = math.pi/180*theta2*1000

#------------------------------------------------- Najprej nardim matriko A
A = []
T = [-2,-1,0,1,2,3,4]
X = [-2,-1,0,1]
l1, l2 = len(T), len(X)
A = []
"""for k in range(len(tab)): #-------------------- Brez mešanih členov
    temp = []
    for j in range(len(T)): 
        m = T[j]
        temp.append(theta1[k]**m)
    for i in range(1,len(X)): 
        n = X[i]
        temp.append( x[k]**n)
    A.append(temp)"""
for k in range(len(tab)): # --------------------- Tudi mešani členi
    temp = []
    for i in range(len(X)): 
        for j in range(len(T)): 
            n = X[i] 
            m = T[j] 
            if n+m>=max(len(X),len(T)):
                break
            else: 
                temp.append( theta1[k]**m * x[k]**n)
    A.append(temp)


U, D, V = np.linalg.svd(A, full_matrices=False)
S = np.diag(D)
X_a = np.matmul(np.matmul(U, np.diag(D)), V)
#print(np.std(A), np.std(X_a), np.std(A - X_a))

#----------------------------------------------------- izracunamo ven fite
N = len(tab)
M = len(A[0])
x1  = 0

for i in range(M):
    temp = np.dot(np.dot(U[:,i].T, theta2.T), V[i,:]) / S[i,i]
    x1 += temp
#H = chisquare(np.matmul(A,x1),theta2)
H = 0
for i in range(len(theta2)):
    H += (theta2[i] - np.dot(A[i],x1))**2/(1)**2

print(len(A[0]),'\t', H/(N-M), '\t', 'T = ',T,'\t','X = ',X,sep='')

#for i in range(len(tab)):
#    print(x[i], theta1[i], theta2[i], np.dot(A[i],x1), sep='\t')
#----------------------------------------------------- rcunam se varianco x-ov

"""M =[]
k = 0
for j in range(2):
    for i in range(2):
        #print(i,j,k)
        M.append(V[i,j]*V[i,k]/ S[i,i]**2)
    k += 1
print(M) """
