import numpy as np
import scipy as sp
import math
import random


random.seed()

def print_stanja(tabela, dt):
    print('"$ \\\Delta t = ', dt, '$"', sep ='')
    for i in range(len(tabela)):
        print(cas[i], tabela[i], sep ='\t')
    print('')
def pos_or_neg():
    return 1 if random.random() < 0.5 else -1
def f(t):
    return N0*np.exp(-beta*t)

beta = 1.0
betar = 4*beta
betas = 5*beta
N0 = 250
dt = 0.001

Rn = dt*betar*np.arange(0,N0+1)
Sn = dt*betas*np.arange(0,N0+1)
M = np.zeros((N0+1,N0+1))


M[0][0] = 1 - (Rn[0] + Sn[0])
M[0][1] = Sn[1] 
M[-1][-2] = Rn[-2]
#M[-1][-1] = 10000 - (Rn[-1] + Sn[-1])
M[-1][-1] = 1 - (Sn[-1])
M = np.matrix(M)

for i in range(1,N0):
    j = i
    M[i,j-1:j+2] = [Rn[i-1], 1 - (Rn[i] + Sn[i]), Sn[i+1]]

x0 = np.zeros(N0+1)
x0[-1] = 1

poteze = 1
eps = 1e-40
for i in range(10000):
    Mpow = np.linalg.matrix_power(M, i)
    X = np.dot(Mpow, x0.T)
    #if np.argmax(X) == 0:
    a = X[0]
    if a - eps == 0:
        cas = i*dt
        break
#print(np.sum(M[:,-1]))
#print(M[:,-1])
print(cas)


konec, dt = 10, 1
cas = np.linspace(0, konec, int(konec/dt)+1)
